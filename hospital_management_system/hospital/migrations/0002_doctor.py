# Generated by Django 4.2.1 on 2023-09-27 07:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=255)),
                ('date_of_birth', models.CharField(max_length=255)),
                ('experience', models.IntegerField()),
                ('age', models.IntegerField()),
                ('phone_nnumber', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('gender', models.CharField(max_length=255)),
                ('about_doctor', models.TextField()),
                ('address', models.TextField()),
                ('image', models.ImageField(upload_to='doctor_image')),
                ('resume', models.FileField(upload_to='doctor_resume')),
                ('specialization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospital.specialization')),
            ],
        ),
    ]
