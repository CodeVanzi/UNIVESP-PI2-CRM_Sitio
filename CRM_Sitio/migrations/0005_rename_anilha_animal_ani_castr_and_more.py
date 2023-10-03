# Generated by Django 4.2.1 on 2023-05-15 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM_Sitio', '0004_auto_20230515_1826'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='anilha',
            new_name='ani_castr',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='chip',
            new_name='ani_cor',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='data_nascimento',
            new_name='ani_dnasc',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='cor',
            new_name='ani_espec',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='foto',
            new_name='ani_foto',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='idade',
            new_name='ani_idade',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='especie',
            new_name='ani_nome',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='nome',
            new_name='ani_porte',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='porte',
            new_name='ani_raça',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='raça',
            new_name='ani_rga',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='rga',
            new_name='ani_sexo',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='castrado',
            new_name='ani_vacinado',
        ),
        migrations.RenameField(
            model_name='animal',
            old_name='vacinado',
            new_name='ani_vermifugado',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='sexo',
        ),
        migrations.RemoveField(
            model_name='animal',
            name='vermifugado',
        ),
        migrations.AddField(
            model_name='animal',
            name='ani_anilha',
            field=models.CharField(default='não informado', max_length=50),
        ),
        migrations.AddField(
            model_name='animal',
            name='ani_nmchip',
            field=models.CharField(default='não informado', max_length=50),
        ),
        migrations.AddField(
            model_name='animal',
            name='ani_obs',
            field=models.CharField(default='não informado', max_length=200),
        ),
    ]
