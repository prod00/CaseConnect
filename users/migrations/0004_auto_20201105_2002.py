# Generated by Django 3.1.1 on 2020-11-05 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20201102_1723'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='resume',
            field=models.FileField(default=None, upload_to='resumes'),
        ),
    ]
