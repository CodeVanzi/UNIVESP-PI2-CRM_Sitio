# Generated by Django 4.2.1 on 2023-05-25 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM_Sitio', '0021_remove_animal_ani_vacinado_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='ani_anilha',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_castr',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_cor',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_espec',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_nmchip',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_nome',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_obs',
            field=models.CharField(blank=True, default='', max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_porte',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_raça',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_sexo',
            field=models.CharField(default='', max_length=50),
        ),
    ]
