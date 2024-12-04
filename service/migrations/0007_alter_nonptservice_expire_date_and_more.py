# Generated by Django 5.1.1 on 2024-10-12 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0006_nonptservice_name_ptservice_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nonptservice',
            name='expire_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='nonptservice',
            name='number_of_month',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='nonptservice',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ptservice',
            name='cost_per_session',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AlterField(
            model_name='ptservice',
            name='expire_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='ptservice',
            name='number_of_session',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ptservice',
            name='session_duration',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ptservice',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]