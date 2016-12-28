# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-21 00:18
from __future__ import unicode_literals

from django.db import migrations, models
import edc_base.utils


class Migration(migrations.Migration):

    dependencies = [
        ('django_crypto_fields', '0003_auto_20161124_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crypt',
            name='created',
            field=models.DateTimeField(default=edc_base.utils.get_utcnow, editable=False),
        ),
        migrations.AlterField(
            model_name='crypt',
            name='modified',
            field=models.DateTimeField(default=edc_base.utils.get_utcnow, editable=False),
        ),
    ]
