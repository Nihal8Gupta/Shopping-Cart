# Generated by Django 5.0.1 on 2024-02-23 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='actual_price',
            field=models.FloatField(null=True),
        ),
    ]