# Generated by Django 4.2.1 on 2023-09-25 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sendemailtomyemail', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactus',
            old_name='name',
            new_name='fname',
        ),
        migrations.RemoveField(
            model_name='contactus',
            name='Content',
        ),
        migrations.AddField(
            model_name='contactus',
            name='lname',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='contactus',
            name='password',
            field=models.CharField(default='None', max_length=20),
        ),
    ]
