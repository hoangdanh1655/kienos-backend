# Generated by Django 5.1.1 on 2024-11-03 06:20

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0011_remove_coachprofile_undertaken_services_and_more'),
        ('workout', '0018_workoutschedule_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workoutschedule',
            name='date',
        ),
        migrations.AddField(
            model_name='workoutschedule',
            name='start_time_temp',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='workoutschedule',
            name='end_time_temp',
            field=models.DateTimeField(null=True, blank=True),
        ),
        
        migrations.RunPython(
            code=migrations.RunPython.noop,  
            reverse_code=migrations.RunPython.noop
        ),
        
        migrations.RemoveField(
            model_name='workoutschedule',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='workoutschedule',
            name='end_time',
        ),
        
        migrations.RenameField(
            model_name='workoutschedule',
            old_name='start_time_temp',
            new_name='start_time',
        ),
        migrations.RenameField(
            model_name='workoutschedule',
            old_name='end_time_temp',
            new_name='end_time',
        ),
    ]
