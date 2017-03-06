# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 18:35
from __future__ import unicode_literals

from django.db import migrations
import edc_base.model_fields.uuid_auto_field


class Migration(migrations.Migration):

    dependencies = [
        ('django_crypto_fields', '0002_crypt_cipher_mode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypt',
            name='id',
            field=edc_base.model_fields.uuid_auto_field.UUIDAutoField(blank=True, editable=False, help_text='System auto field. UUID primary key.', primary_key=True, serialize=False),
        ),
    ]
