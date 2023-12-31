from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddAnimalForm, UpdateAnimalForm, AddVacinaForm, UpdateVacinaForm
from .models.animais import Animal
from .models.vacinas import Vacina
from django.contrib.auth.decorators import login_required
from rolepermissions.roles import assign_role
from rolepermissions.decorators import has_role_decorator, has_permission_decorator
from .roles import Morador, Sindico
from django.contrib.auth.models import User
from rolepermissions.checkers import has_permission
from rolepermissions.checkers import has_role
from django.urls import reverse
from datetime import datetime, timedelta, date
from django.core.exceptions import ObjectDoesNotExist

def home(request):
    if request.user.is_authenticated:
        return redirect('main')
    return render(request, 'home.html')


@login_required
def main(request):
    if has_permission(request.user, 'can_see_all_animals'):
        animals = Animal.objects.all()
    else:
        animals = Animal.objects.filter(tutor=request.user)
    return render(request, 'main.html', {'animals': animals})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Você está logado.")
            return redirect('home')
        else:
            messages.error(request, "Usuário ou senha inválidos. Por favor, tente novamente.")
            return redirect('login')

    return render(request, 'login.html')

@login_required
def logout_user(request):
    logout(request)
    messages.success(request, "Você saiu da sua conta...")
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            assign_role(user, Morador)
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            
            messages.success(request, "Você foi registrado com sucesso. Bem-vindo!")
            return redirect('main')
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})

def register_admin(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            assign_role(user, Sindico)
            
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            
            messages.success(request, "Você foi registrado com sucesso. Bem-vindo!")
            return redirect('main')
    else:
        form = SignUpForm()
    
    return render(request, 'register.html', {'form': form})

@login_required
@has_permission_decorator('can_delete_animal')
def delete_animal(request, pk):
    delete_it = get_object_or_404(Animal, id=pk)

    if has_role(request.user, 'sindico') or delete_it.tutor == request.user:
        delete_it.delete()
        messages.success(request, "Animal deletado com sucesso!")
        return redirect('home')
    else:
        messages.error(request, "Você não tem permissão para excluir este animal.")
        return redirect('home')

@login_required
@has_permission_decorator('can_add_animal')
def add_animal(request):
    if request.method == "POST":
        form = AddAnimalForm(request.POST, request.FILES)
        if form.is_valid():
            animal_data = form.cleaned_data
            animal = Animal(**animal_data)
            animal.tutor = request.user
            animal._request = request  # Define o atributo _request com o valor da requisição
            animal.save()
            messages.success(request, "Animal adicionado com sucesso")
            return redirect('animal_profile', pk=animal.pk)
        else:
            messages.error(request, "Formulário inválido")
    else:
        form = AddAnimalForm()
    return render(request, 'add_animal.html', {'form': form})



@login_required
@has_permission_decorator('can_update_animal')
def update_animal(request, pk):
    current_animal = get_object_or_404(Animal, id=pk)

    if has_role(request.user, 'sindico') or current_animal.tutor == request.user:
        if request.method == 'POST':
            form = UpdateAnimalForm(request.POST, request.FILES, instance=current_animal)
            if form.is_valid():
                form.save()
                messages.success(request, "Animal atualizado")
                return redirect('animal_profile', pk=pk)
        else:
            form = UpdateAnimalForm(instance=current_animal)

        context = {
            'form': form,
            'current_animal': current_animal
        }
        return render(request, 'update_animal.html', context)
    else:
        messages.error(request, "Você não tem permissão para atualizar este animal.")
        return redirect('home')

@login_required
def pet_list(request):
    if has_permission(request.user, 'can_see_all_animals'):
        animals = Animal.objects.all()
    else:
        animals = Animal.objects.filter(tutor=request.user)

    pet_info_list = []
    
    for animal in animals:
        possui_vacina_raiva = False
        possui_vermifugo = False

        if Vacina.objects.filter(animal=animal, vac_tipo__in=['V8 ou V10']).exists():
            vacina_recente = Vacina.objects.filter(animal=animal, vac_tipo__in=['V8 ou V10']).order_by('vac_data_admin').first()
            if date.today() <= (vacina_recente.vac_data_admin + timedelta(days=365)):
                possui_vacina_raiva = True

        if Vacina.objects.filter(animal=animal, vac_tipo__in=['Vermífugo']).exists():    
            vermifugo_recente = Vacina.objects.filter(animal=animal, vac_tipo__in=['Vermífugo']).order_by('vac_data_admin').first()
            if date.today() <= (vermifugo_recente.vac_data_admin + timedelta(days=183)):
                possui_vermifugo = True

            
        info = {
            'animals': animal,
            'possui_vacina_raiva': possui_vacina_raiva,
            'possui_vermifugo': possui_vermifugo
        }
        pet_info_list.append(info)

    context = {
        'animals': animals,
        'pet_info_list': pet_info_list
    }

    return render(request, 'pet_list.html', context)

@login_required
@has_permission_decorator('can_see_animal')
def animal_profile(request, pk):
    animal = get_object_or_404(Animal, id=pk)
    
    if has_role(request.user, 'sindico') or animal.tutor == request.user:
        pet_info_list = []
    
        possui_vacina_raiva = False
        possui_vermifugo = False

        if Vacina.objects.filter(animal=animal, vac_tipo__in=['V8 ou V10']).exists():
            vacina_recente = Vacina.objects.filter(animal=animal, vac_tipo__in=['V8 ou V10']).order_by('vac_data_admin').first()
            if date.today() <= (vacina_recente.vac_data_admin + timedelta(days=365)):
                possui_vacina_raiva = True

        if Vacina.objects.filter(animal=animal, vac_tipo__in=['Vermífugo']).exists():    
            vermifugo_recente = Vacina.objects.filter(animal=animal, vac_tipo__in=['Vermífugo']).order_by('vac_data_admin').first()
            if date.today() <= (vermifugo_recente.vac_data_admin + timedelta(days=183)):
                possui_vermifugo = True
            
        info = {
            'animal': animal,
            'possui_vacina_raiva': possui_vacina_raiva,
            'possui_vermifugo': possui_vermifugo
        }
        pet_info_list.append(info)
        
        context = {
            'animal': animal,
            'pet_info_list': pet_info_list
        }
        
        return render(request, 'animal_profile.html', context)
    
    else:
        messages.error(request, "Você não tem permissão para ver este animal")
        return redirect('home')

@login_required
@has_permission_decorator('can_see_animal')
def add_vacina(request, pk):
    animal = get_object_or_404(Animal, id=pk)

    if has_role(request.user, 'sindico') or animal.tutor == request.user:
        if request.method == 'POST':
            form = AddVacinaForm(request.POST, request.FILES)
            if form.is_valid():
                vacina = form.save(commit=False)
                vacina.animal = animal
                vacina.save()
                messages.success(request, "Vacina adicionada com sucesso")
                return redirect('animal_profile', pk=pk)
        else:
            form = AddVacinaForm()
        return render(request, 'add_vacina.html', {'animal': animal, 'form': form})
    else:
        messages.error(request, "Você não tem permissão para ver este animal")
        return redirect('home')

@login_required
@has_permission_decorator('can_see_animal')
def vacinas_list(request, pk):
    animal = get_object_or_404(Animal, id=pk)
    
    if has_role(request.user, 'sindico') or animal.tutor == request.user:
        vacinas = animal.vacinas.all()
        return render(request, 'vacinas_list.html', {'animal': animal, 'vacinas': vacinas})
    else:
        messages.error(request, "Você não tem permissão para ver as vacinas deste animal")
        return redirect('home')
    
@login_required
@has_permission_decorator('can_update_animal')
def update_vacina(request, pk):
    current_vacina = get_object_or_404(Vacina, vac_id=pk)

    if has_role(request.user, 'sindico') or current_vacina.animal.tutor == request.user:
        if request.method == 'POST':
            form = UpdateVacinaForm(request.POST, request.FILES, instance=current_vacina)
            if form.is_valid():
                vacina = form.save(commit=False)
                if not form.cleaned_data['vac_anexo']:
                    vacina.vac_anexo = current_vacina.vac_anexo
                vacina.save()
                messages.success(request, "Vacina atualizada")
                return redirect(reverse('vacinas_list', kwargs={'pk': current_vacina.animal.id}))
        else:
            form = UpdateVacinaForm(instance=current_vacina)

        return render(request, 'update_vacina.html', {'form': form, 'current_vacina': current_vacina})
    else:
        messages.error(request, "Você não tem permissão para atualizar esta vacina.")
        return redirect('home')

    
@login_required
@has_permission_decorator('can_delete_animal')
def delete_vacina(request, pk):
    current_vacina = get_object_or_404(Vacina, vac_id=pk)

    if has_role(request.user, 'sindico') or current_vacina.animal.tutor == request.user:
        current_vacina.delete()
        messages.success(request, "Vacina excluída")
        return redirect('vacinas_list', pk=current_vacina.animal.id)
    else:
        messages.error(request, "Você não tem permissão para excluir esta vacina.")
        return redirect('vacinas_list', pk=current_vacina.animal.id)
