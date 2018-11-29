# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-11-13 13:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_remove_discussion_picture'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comments',
            old_name='file',
            new_name='image',
        ),
        migrations.AddField(
            model_name='discussion',
            name='picture',
            field=models.FileField(default='', upload_to=''),
        ),
    ]