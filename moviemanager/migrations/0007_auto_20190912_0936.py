# Generated by Django 2.2.3 on 2019-09-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moviemanager', '0006_auto_20190912_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookings',
            name='email',
            field=models.EmailField(max_length=100),
        ),
    ]
