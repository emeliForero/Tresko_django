# Generated by Django 4.2.5 on 2023-09-30 06:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_alter_userprofile_role'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='city',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='firm',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='gender',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='identification',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='role',
        ),
    ]