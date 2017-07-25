# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-02-10 01:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('budgetapp', '0003_auto_20170130_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='owner',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='categories', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]