# Generated by Django 4.2.5 on 2023-09-10 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_folder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateTimeField(auto_now=True, verbose_name='last login'),
        ),
    ]
