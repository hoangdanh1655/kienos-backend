# Generated by Django 5.1.1 on 2024-10-12 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0008_alter_nonptservice_name_alter_ptservice_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nonptservice',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='ptservice',
            name='coach',
        ),
        migrations.RemoveField(
            model_name='ptservice',
            name='customer',
        ),
    ]
