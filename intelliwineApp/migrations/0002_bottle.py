# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-11 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intelliwineApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('color', models.CharField(choices=[(b'0', b'red'), (b'1', b'white'), (b'2', b'pink'), (b'3', b'gold')], max_length=10)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
