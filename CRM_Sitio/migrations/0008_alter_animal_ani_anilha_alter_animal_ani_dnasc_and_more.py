# Generated by Django 4.2.1 on 2023-05-19 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM_Sitio', '0007_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='ani_anilha',
            field=models.CharField(blank=True, default='não informado', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_dnasc',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_foto',
            field=models.ImageField(blank=True, default='', null=True, upload_to='media/animais/'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_idade',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_nmchip',
            field=models.CharField(blank=True, default='não informado', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_obs',
            field=models.CharField(blank=True, default='não informado', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_rga',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_vacinado',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='animal',
            name='ani_vermifugado',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]