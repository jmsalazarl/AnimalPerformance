# Generated by Django 3.1.7 on 2021-03-21 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appAnimalPerformance', '0007_auto_20210320_2249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='peso_producto',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5, null=True),
        ),
    ]
