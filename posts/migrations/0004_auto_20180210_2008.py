

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20180210_0522'),
    ]

    operations = [
        migrations.CreateModel(
            name='LastUpdate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('updated', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='disabled',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='audience',
            field=models.EnumField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='locale',
            field=models.EnumField(default=1),
        ),
    ]
