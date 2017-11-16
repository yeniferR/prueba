# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2017-11-13 19:16
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='trabaj',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('email', models.EmailField(default='description email', max_length=254, validators=[django.core.validators.EmailValidator(message='Ingresa un email valido')])),
                ('comentario', models.TextField(default='description default text')),
            ],
        ),
    ]
