# Generated by Django 5.1.1 on 2024-10-14 08:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0007_alter_coachprofile_undertaken_services'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='coach',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customers', to='user_profile.coachprofile'),
        ),
    ]
