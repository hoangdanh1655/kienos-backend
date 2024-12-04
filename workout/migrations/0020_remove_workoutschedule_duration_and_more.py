# Generated by Django 5.1.1 on 2024-11-03 10:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0012_customerprofile_health_condition'),
        ('workout', '0019_remove_workoutschedule_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutschedule',
            name='duration',
        ),
        migrations.RemoveField(
            model_name='workoutschedule',
            name='exercises',
        ),
        migrations.RemoveField(
            model_name='workoutschedule',
            name='note',
        ),
        migrations.RemoveField(
            model_name='workoutschedule',
            name='overview',
        ),
        migrations.CreateModel(
            name='TrainingPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estimated_duration', models.IntegerField(default=0)),
                ('overview', models.TextField(blank=True, null=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer_training_plans', to='user_profile.customerprofile')),
                ('exercises', models.ManyToManyField(related_name='exercise', to='workout.exercise')),
            ],
            options={
                'db_table': 'training_plan',
            },
        ),
        migrations.AddField(
            model_name='workoutschedule',
            name='training_plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='workout.trainingplan'),
        ),
    ]