# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-15 19:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('intelliwineApp', '0009_auto_20160615_1928'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bottlevectorcharacteristics',
            old_name='charac_foreign_key',
            new_name='bottle_foreign_key',
        ),
        migrations.RenameField(
            model_name='bottlevectorflavourandaroma',
            old_name='flav_aroma_foreign_key',
            new_name='bottle_foreign_key',
        ),
    ]
