# Generated by Django 3.2.4 on 2022-04-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0007_alter_serviceprovider_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceprovider',
            name='account',
            field=models.CharField(choices=[('COMPANY', 'company'), ('INDIVIDUAL', 'individual')], max_length=20),
        ),
    ]
