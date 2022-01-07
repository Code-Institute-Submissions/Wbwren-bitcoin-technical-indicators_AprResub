# Generated by Django 3.2 on 2022-01-05 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0005_auto_20220105_2024'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='metric_data',
            name='ma50d_50w',
        ),
        migrations.AddField(
            model_name='metric_data',
            name='ma50d_200d',
            field=models.FloatField(blank=True, null=True, verbose_name='ma50d_200d'),
        ),
    ]
