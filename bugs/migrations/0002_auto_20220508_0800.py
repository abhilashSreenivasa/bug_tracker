# Generated by Django 3.0.9 on 2022-05-08 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bugs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Bugs',
            new_name='Bug',
        ),
    ]
