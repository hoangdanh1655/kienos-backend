# Generated by Django 5.1.1 on 2024-10-18 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0006_delete_workoutplan'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutschedule',
            name='exercise',
        ),
        migrations.AddField(
            model_name='workoutschedule',
            name='exercises',
            field=models.ManyToManyField(related_name='exercise', to='workout.exercise'),
        ),
    ]
