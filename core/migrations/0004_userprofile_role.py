# Generated by Django 3.0.9 on 2022-05-07 23:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20220507_2307'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='role',
            field=models.ForeignKey(default='Manager', on_delete=django.db.models.deletion.CASCADE, to='core.Role'),
            preserve_default=False,
        ),
    ]