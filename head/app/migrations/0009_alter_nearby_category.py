# Generated by Django 3.2.23 on 2023-11-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_nearby_nearby_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nearby',
            name='category',
            field=models.CharField(choices=[('Hotel', 'Hotel'), ('Museums', 'Museums'), ('Restaurant', 'Restaurant'), ('Shop', 'Shop'), ('Home', 'Home')], max_length=100, verbose_name='Category'),
        ),
    ]