# Generated by Django 4.2.1 on 2023-09-27 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0002_doctor'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='status',
            field=models.CharField(choices=[('Available', 'Available'), ('Not Available', 'Not Available'), ('On Leave', 'On Leave')], default='Available', max_length=50),
        ),
    ]
