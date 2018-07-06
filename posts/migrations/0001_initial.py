# Generated by Django 2.0.2 on 2018-02-10 04:40

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
                ('author', models.IntField(default = 2))
                ('published', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('audience', models.Enum(default = 1)),
                ('image_url', models.URLField(default='')),
                ('content', models.CharField(max_length=30000)),
                ('disabled', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('locale'), models.CharField(max_length=30),
                ('language'),models.Enum(default = 1)
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
