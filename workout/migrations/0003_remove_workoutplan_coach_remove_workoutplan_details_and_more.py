# Generated by Django 5.1.1 on 2024-09-21 11:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0003_nonptservice_ptservice'),
        ('workout', '0002_alter_exercise_table_alter_workoutgoal_table_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutplan',
            name='coach',
        ),
        migrations.RemoveField(
            model_name='workoutplan',
            name='details',
        ),
        migrations.RemoveField(
            model_name='workoutplan',
            name='expire_date',
        ),
        migrations.RemoveField(
            model_name='workoutplan',
            name='start_date',
        ),
        migrations.AddField(
            model_name='workoutplan',
            name='nonptservice_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.nonptservice'),
        ),
        migrations.AddField(
            model_name='workoutplan',
            name='ptservice_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='service.ptservice'),
        ),
        migrations.AlterField(
            model_name='workoutplan',
            name='customer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='workout_plans', to=settings.AUTH_USER_MODEL),
        ),
    ]
