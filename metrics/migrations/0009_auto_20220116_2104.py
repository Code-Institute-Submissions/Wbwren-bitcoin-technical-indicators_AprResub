# Generated by Django 3.2 on 2022-01-16 21:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0008_metric_image_path'),
    ]

    operations = [
        migrations.RenameField(
            model_name='metric',
            old_name='description',
            new_name='description_long',
        ),
        migrations.AddField(
            model_name='metric',
            name='description_short',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]