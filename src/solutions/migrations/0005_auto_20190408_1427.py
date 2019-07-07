# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-08 14:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solutions', '0004_typo_corrections'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solution',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.User', verbose_name='solution author'),
        ),
    ]
