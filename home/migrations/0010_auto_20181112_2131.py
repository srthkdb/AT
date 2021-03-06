# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-12 21:31
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0009_subjects_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subjects',
            name='user',
        ),
        migrations.AddField(
            model_name='comments',
            name='user_comment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='discussion',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
