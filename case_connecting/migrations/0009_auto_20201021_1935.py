# Generated by Django 3.1.1 on 2020-10-21 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case_connecting', '0008_auto_20201021_1934'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='post',
            field=models.DateTimeField(),
        ),
    ]
