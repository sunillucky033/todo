# Generated by Django 3.0.5 on 2020-04-21 04:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='date',
        ),
    ]
