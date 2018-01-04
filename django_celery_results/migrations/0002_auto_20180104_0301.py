# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-04 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('celery_results', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskresult',
            name='task_args',
            field=models.TextField(blank=True, default='', verbose_name='task arguments'),
        ),
        migrations.AddField(
            model_name='taskresult',
            name='task_kwargs',
            field=models.TextField(blank=True, default='', verbose_name='task keyword arguments'),
        ),
        migrations.AddField(
            model_name='taskresult',
            name='task_name',
            field=models.CharField(blank=True, default='', max_length=255, verbose_name='task name'),
        ),
    ]