# Generated by Django 3.1.1 on 2020-10-21 19:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('case_connecting', '0009_auto_20201021_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='post',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='case_connecting.post'),
        ),
    ]
