

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20180211_1517'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lastupdate',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
