# Generated by Django 3.2 on 2022-01-04 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metrics', '0002_bitcoin_price_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitcoin_price_data',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]