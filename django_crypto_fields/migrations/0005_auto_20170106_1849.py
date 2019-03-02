# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-01-06 16:49
from __future__ import unicode_literals

from django.db import migrations, models
import edc_model_fields.fields.hostname_modification_field
import edc_model_fields.fields.userfield
from edc_utils import get_utcnow


class Migration(migrations.Migration):

    dependencies = [("django_crypto_fields", "0004_auto_20161221_0018")]

    operations = [
        migrations.AlterField(
            model_name="crypt",
            name="created",
            field=models.DateTimeField(blank=True, default=get_utcnow),
        ),
        migrations.AlterField(
            model_name="crypt",
            name="hostname_created",
            field=models.CharField(
                blank=True,
                default="mac2-2.local",
                help_text="System field. (modified on create only)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="crypt",
            name="hostname_modified",
            field=edc_model_fields.fields.hostname_modification_field.HostnameModificationField(
                blank=True,
                help_text="System field. (modified on every save)",
                max_length=50,
            ),
        ),
        migrations.AlterField(
            model_name="crypt",
            name="modified",
            field=models.DateTimeField(blank=True, default=get_utcnow),
        ),
        migrations.AlterField(
            model_name="crypt",
            name="user_created",
            field=edc_model_fields.fields.userfield.UserField(
                blank=True, max_length=50, verbose_name="user created"
            ),
        ),
        migrations.AlterField(
            model_name="crypt",
            name="user_modified",
            field=edc_model_fields.fields.userfield.UserField(
                blank=True, max_length=50, verbose_name="user modified"
            ),
        ),
    ]
