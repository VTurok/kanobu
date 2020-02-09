# Generated by Django 3.0.3 on 2020-02-09 17:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_create', models.DateTimeField(auto_created=True, verbose_name='Дата создания')),
                ('title', models.CharField(db_index=True, max_length=150, verbose_name='Заголовок')),
                ('body', models.TextField(blank=True, db_index=True, verbose_name='Текст статьи')),
                ('date_pub', models.DateTimeField(auto_now=True, verbose_name='Дата публикации')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
        ),
    ]