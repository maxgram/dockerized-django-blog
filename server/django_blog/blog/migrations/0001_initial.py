# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-22 18:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Slug')),
                ('previewText', models.CharField(max_length=255, verbose_name='Preview Txt')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('body', models.TextField(max_length=5000, verbose_name='Body')),
                ('is_published', models.BooleanField(default=True, verbose_name='Published')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='Date Published')),
            ],
            options={
                'ordering': ['-pub_date'],
                'verbose_name': 'Blog Post',
                'verbose_name_plural': 'All Posts',
            },
        ),
    ]