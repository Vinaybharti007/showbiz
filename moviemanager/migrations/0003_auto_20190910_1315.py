# Generated by Django 2.2.3 on 2019-09-10 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviemanager', '0002_auto_20190910_1206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
