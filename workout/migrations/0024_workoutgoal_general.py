# Generated by Django 5.1.1 on 2024-11-12 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0023_alter_exercise_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='workoutgoal',
            name='general',
            field=models.CharField(blank=True, null=True),
        ),
    ]
