# Generated by Django 3.2.23 on 2023-11-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_nearby'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='id',
        ),
        migrations.AddField(
            model_name='place',
            name='place_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
