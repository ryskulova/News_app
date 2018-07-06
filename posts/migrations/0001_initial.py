

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
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author',models.ForeignKey (on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_AUTHOR_MODEL, unique=True)),
                ('audience', models.EnumField(default = 1)),
                ('image', models.CharField(max_length=200)),
                ('disabled', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('locale'), models.CharField(default=1),

                ],
        ),

    ]

   operations = [
       migrations.CreateModel(
           name='NewsContent',
           fields=[
               ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
               ('title', models.CharField (max_length=200)),
               ('content', models.CharField(max_length=30000)),
               ('locale'), models.EnumField (default=1),
               ('timestamp', models.DateTimeField(auto_now_add=True)),
           ]
       )
   ]


operations = [
       migrations.CreateModel(
           name='NewsLanguages',
           fields=[
               ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
               ('locale'), models.EnumField (default=1),
               ]
       )
   ]