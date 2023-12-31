# Generated by Django 3.2.23 on 2023-11-03 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='address',
            field=models.CharField(default='default_text', max_length=500, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='desc',
            field=models.CharField(default='default_text', max_length=500, verbose_name='Description'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='lat',
            field=models.CharField(default='default_text', max_length=100, verbose_name='Latitude'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='place',
            name='long',
            field=models.CharField(default='default_text', max_length=100, verbose_name='Longitude'),
            preserve_default=False,
        ),
    ]
