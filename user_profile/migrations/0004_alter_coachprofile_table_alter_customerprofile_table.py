# Generated by Django 5.1.1 on 2024-09-19 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0003_alter_customerprofile_last_name'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='coachprofile',
            table='coach_profile',
        ),
        migrations.AlterModelTable(
            name='customerprofile',
            table='customer_profile',
        ),
    ]