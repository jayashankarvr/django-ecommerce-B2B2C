# Generated by Django 3.2.4 on 2022-05-31 14:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ordering', '0019_quotation_reference'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quotation',
            old_name='reference',
            new_name='reference_number',
        ),
    ]