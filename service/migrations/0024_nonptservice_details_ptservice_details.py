# Generated by Django 5.1.1 on 2024-12-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0023_nonptservice_discount_end_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='nonptservice',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ptservice',
            name='details',
            field=models.TextField(blank=True, null=True),
        ),
    ]
