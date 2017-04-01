# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-01 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=40, verbose_name='Название проекта')),
                ('title', models.TextField(verbose_name='Заголовок')),
                ('title_description', models.TextField(blank=True, null=True, verbose_name='Текст под заголовком')),
                ('title_btn', models.CharField(default='Learn', max_length=50, verbose_name='Текст кнопки')),
                ('title_btn_url', models.CharField(blank=True, max_length=50, null=True, verbose_name='URL кнопки')),
                ('content', models.TextField(blank=True, null=True, verbose_name='Контент')),
            ],
        ),
    ]
