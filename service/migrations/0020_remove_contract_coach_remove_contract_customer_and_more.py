# Generated by Django 5.1.1 on 2024-10-24 00:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0019_alter_contract_coach_alter_contract_customer'),
        ('user_profile', '0011_remove_coachprofile_undertaken_services_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contract',
            name='coach',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='customer',
        ),
        migrations.AddField(
            model_name='contract',
            name='coach',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='coach_contracts', to='user_profile.coachprofile'),
        ),
        migrations.AddField(
            model_name='contract',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_contracts', to='user_profile.customerprofile'),
        ),
    ]
