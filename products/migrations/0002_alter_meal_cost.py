# Generated by Django 4.2.9 on 2024-02-02 01:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=15, verbose_name='Ovqat narxi(UZS):'),
        ),
    ]
