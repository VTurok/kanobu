# Generated by Django 3.0.3 on 2020-02-09 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("materials", "0003_auto_20200209_2307"),
    ]

    operations = [
        migrations.AlterField(
            model_name="material",
            name="author",
            field=models.ForeignKey(
                blank=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
                verbose_name="Автор",
            ),
        ),
    ]
