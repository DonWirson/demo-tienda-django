# Generated by Django 3.1.6 on 2021-02-18 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='venta',
            options={'verbose_name': 'Venta', 'verbose_name_plural': 'Ventas'},
        ),
        migrations.AddField(
            model_name='producto',
            name='descripcion',
            field=models.CharField(default='No hay descripción', max_length=200),
        ),
    ]
