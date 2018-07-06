

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
                #('published', models.BooleanField(default=False)),
                ('title', models.CharField(max_length=200)),
                ('audience', models.EnumField(default = 1)),
                ('image', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=30000)),
                ('disabled', models.BooleanField(default=False)),
                #('updated', models.DateTimeField(auto_now=True)), #update func/button
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('locale'), models.CharField(max_length=30),
                ('language'),models.EnumField(default = 1),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_AUTHOR_MODEL, unique=True)),
            ],
        ),
    ]
