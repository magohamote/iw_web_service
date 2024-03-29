# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-06-15 19:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intelliwineApp', '0008_remove_bottlevectorflavourandaroma_bottle_charac'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bottle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bottle_name', models.CharField(max_length=256)),
            ],
        ),
        migrations.AddField(
            model_name='bottlevectorcharacteristics',
            name='charac_foreign_key',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='charac', to='intelliwineApp.Bottle'),
        ),
        migrations.AddField(
            model_name='bottlevectorflavourandaroma',
            name='flav_aroma_foreign_key',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='flav_aroma', to='intelliwineApp.Bottle'),
        ),
    ]
