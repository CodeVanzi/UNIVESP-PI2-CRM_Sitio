# Generated by Django 4.2.1 on 2023-05-11 01:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("CRM_Sitio", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="animal",
            old_name="name",
            new_name="nome",
        ),
        migrations.AlterField(
            model_name="animal",
            name="id",
            field=models.BigAutoField(
                auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
            ),
        ),
    ]
