# Generated by Django 4.2.6 on 2023-10-31 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('migraciones', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='preciohistoricovehiculo',
            name='color',
            field=models.CharField(default='Desconocido', max_length=50),
        ),
        migrations.AlterField(
            model_name='preciohistoricovehiculo',
            name='modelo',
            field=models.TextField(verbose_name='Modelo'),
        ),
    ]
