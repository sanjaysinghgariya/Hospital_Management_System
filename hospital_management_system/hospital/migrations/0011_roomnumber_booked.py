# Generated by Django 4.2.1 on 2023-09-29 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0010_room_info_roomnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomnumber',
            name='booked',
            field=models.BooleanField(default=False),
        ),
    ]
