# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-30 04:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zerver', '0124_stream_enable_notifications'),
    ]

    operations = [
        migrations.AddField(
            model_name='realm',
            name='max_invites',
            field=models.IntegerField(default=100),
        ),
    ]