# Generated by Django 5.1.1 on 2024-10-21 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workout', '0009_remove_workoutgoal_coach_remove_workoutgoal_customer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to='media/exercises/'),
        ),
    ]
