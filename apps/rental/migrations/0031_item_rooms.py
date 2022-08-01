# Generated by Django 3.2.4 on 2022-04-19 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rental', '0030_room'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='rooms',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='rental.room'),
        ),
    ]