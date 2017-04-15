# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-05 13:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0089_create_project_manager_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]