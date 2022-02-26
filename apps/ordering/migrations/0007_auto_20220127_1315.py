# Generated by Django 3.2.4 on 2022-01-27 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0006_auto_20220111_1234'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='subtotal',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=13),
        ),
        migrations.AddField(
            model_name='order',
            name='vat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=100),
        ),
    ]