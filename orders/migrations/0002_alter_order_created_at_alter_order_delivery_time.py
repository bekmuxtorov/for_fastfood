# Generated by Django 4.2.9 on 2024-02-01 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name="Qo'shilgan vaqt"),
        ),
        migrations.AlterField(
            model_name='order',
            name='delivery_time',
            field=models.DateField(verbose_name='Tahminiy yetkazib berish vaqti'),
        ),
    ]