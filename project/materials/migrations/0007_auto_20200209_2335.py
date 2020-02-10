# Generated by Django 3.0.3 on 2020-02-09 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0006_auto_20200209_2332"),
    ]

    operations = [
        migrations.AlterField(
            model_name="material",
            name="material_type",
            field=models.CharField(
                choices=[("Новость", "Новость"), ("Статья", "Статья")],
                max_length=7,
                verbose_name="Тип материала",
            ),
        ),
    ]