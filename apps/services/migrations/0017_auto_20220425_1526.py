# Generated by Django 3.2.4 on 2022-04-25 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0016_alter_serviceprovider_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serviceprovider',
            name='daily_rate',
        ),
        migrations.DeleteModel(
            name='Daily_rate',
        ),
    ]