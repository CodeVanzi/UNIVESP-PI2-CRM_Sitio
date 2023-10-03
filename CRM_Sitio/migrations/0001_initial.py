# Generated by Django 4.2.1 on 2023-05-07 02:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Animal",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("idade", models.IntegerField()),
                ("data_nascimento", models.DateField()),
                ("data_cadastro", models.DateField(auto_now_add=True)),
                ("cor", models.CharField(max_length=50)),
                ("foto", models.ImageField(upload_to="")),
                ("rga", models.CharField(max_length=50)),
                ("castrado", models.BooleanField()),
                ("anilha", models.CharField(max_length=50)),
                ("chip", models.CharField(max_length=50)),
                ("vacinado", models.BooleanField()),
                ("vermifugado", models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name="Especie",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Porte",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Raça",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Sexo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="Vacina",
            fields=[
                ("vac_id", models.AutoField(primary_key=True, serialize=False)),
                ("vac_nome", models.CharField(max_length=50)),
                ("vac_data_admin", models.DateField()),
                ("vac_num_dose", models.IntegerField()),
                ("vac_fabricante", models.CharField(max_length=50)),
                ("vac_validade", models.DateField()),
                (
                    "animal_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="CRM_Sitio.animal",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Tutor",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("profile_picture", models.ImageField(upload_to="")),
                (
                    "nome",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="animal",
            name="especie",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="CRM_Sitio.especie",
            ),
        ),
        migrations.AddField(
            model_name="animal",
            name="porte",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="CRM_Sitio.porte",
            ),
        ),
        migrations.AddField(
            model_name="animal",
            name="raça",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="CRM_Sitio.raça",
            ),
        ),
        migrations.AddField(
            model_name="animal",
            name="sexo",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="CRM_Sitio.sexo",
            ),
        ),
        migrations.AddField(
            model_name="animal",
            name="tutor",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="CRM_Sitio.tutor",
            ),
        ),
    ]
