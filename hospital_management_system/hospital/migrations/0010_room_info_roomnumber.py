# Generated by Django 4.2.1 on 2023-09-29 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0009_appointment_visit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Room_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('types_of_room', models.CharField(default='General Ward Room', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='RoomNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_number', models.CharField(default='001', max_length=20)),
                ('type_of_room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.room_info')),
            ],
        ),
    ]
