# Generated by Django 4.2.4 on 2023-11-26 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accommodations',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='accommodations', verbose_name='Imagen 1'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='accommodations', verbose_name='Imagen 2'),
        ),
        migrations.AlterField(
            model_name='accommodations',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='accommodations', verbose_name='Imagen 3'),
        ),
    ]