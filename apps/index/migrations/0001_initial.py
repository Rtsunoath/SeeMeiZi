# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-12-05 01:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Feeds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='标题')),
                ('image_url', models.CharField(max_length=100, verbose_name='图片链接')),
            ],
            options={
                'verbose_name': '动态',
                'verbose_name_plural': '动态',
            },
        ),
    ]
