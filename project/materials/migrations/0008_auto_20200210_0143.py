# Generated by Django 3.0.3 on 2020-02-09 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("materials", "0007_auto_20200209_2335"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="date_create",
            field=models.DateTimeField(auto_now_add=True, verbose_name="Дата создания"),
        ),
    ]
