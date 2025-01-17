# Generated by Django 5.1.1 on 2024-10-09 10:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_nonptservice_ptservice'),
        ('user_profile', '0005_remove_coachprofile_phone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonptservice',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registered_nonptservice', to='user_profile.customerprofile'),
        ),
        migrations.AddField(
            model_name='ptservice',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coach_for', to='user_profile.coachprofile'),
        ),
        migrations.AddField(
            model_name='ptservice',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='registered_ptservice', to='user_profile.customerprofile'),
        ),
    ]
