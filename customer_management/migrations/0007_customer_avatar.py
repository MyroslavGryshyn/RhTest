# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-12 09:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer_management', '0006_auto_20160510_1301'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='avatar',
            field=models.ImageField(default=0, upload_to=''),
            preserve_default=False,
        ),
    ]