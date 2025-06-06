# Generated by Django 5.1.9 on 2025-05-28 17:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("escoladjango", "0002_matricula"),
    ]

    operations = [
        migrations.AlterField(
            model_name="curso",
            name="codigo",
            field=models.CharField(
                max_length=10,
                unique=True,
                validators=[django.core.validators.MinLengthValidator(3)],
            ),
        ),
        migrations.AlterField(
            model_name="estudante",
            name="numero_celular",
            field=models.CharField(max_length=13),
        ),
    ]
