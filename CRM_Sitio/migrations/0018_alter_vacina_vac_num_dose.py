# Generated by Django 4.2.1 on 2023-05-24 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CRM_Sitio', '0017_vacina_vac_anexo_vacina_vac_tipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacina',
            name='vac_num_dose',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]