# Generated by Django 4.2.1 on 2023-05-21 16:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('CRM_Sitio', '0014_alter_animal_data_cadastro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='tutor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pets', to=settings.AUTH_USER_MODEL),
        ),
    ]
