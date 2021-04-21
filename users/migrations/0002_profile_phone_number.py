# Generated by Django 3.0.6 on 2021-04-16 05:35

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default='', max_length=128, region=None),
            preserve_default=False,
        ),
    ]