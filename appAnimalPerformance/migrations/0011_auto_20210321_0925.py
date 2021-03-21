# Generated by Django 3.1.7 on 2021-03-21 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAnimalPerformance', '0010_auto_20210320_2355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='porcentaje_peso_producto',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='total_costo_producto',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='total_venta_producto',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='utilidad_producto',
            field=models.FloatField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='producto',
            name='utilidad_producto_xKG',
            field=models.FloatField(blank=True, default=0),
        ),
    ]
