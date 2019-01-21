# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("django_crypto_fields", "0001_initial")]

    operations = [
        migrations.AddField(
            model_name="crypt",
            name="cipher_mode",
            field=models.IntegerField(
                help_text="pycrypto AES cipher mode (e.g. MODE_CBC)", null=True
            ),
        )
    ]
