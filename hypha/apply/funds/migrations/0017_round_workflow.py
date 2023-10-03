# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-08 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("funds", "0016_roundform"),
    ]

    operations = [
        migrations.AddField(
            model_name="round",
            name="workflow",
            field=models.CharField(
                choices=[("single", "Single Stage"), ("double", "Two Stage")],
                default="single",
                max_length=100,
            ),
        ),
    ]
