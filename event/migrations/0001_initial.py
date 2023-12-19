# Generated by Django 4.2.4 on 2023-11-23 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id_event', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='Nombre Evento')),
                ('date_event', models.DateTimeField(verbose_name='Fecha Evento')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('mainImage', models.ImageField(upload_to='events', verbose_name='Imagen Portada')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'Evento',
                'verbose_name_plural': 'Eventos',
                'ordering': ['-created'],
            },
        ),
    ]