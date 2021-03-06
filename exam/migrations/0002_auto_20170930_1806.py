# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 15:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Round',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='examiner',
            name='code',
            field=models.CharField(default=0, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examiner',
            name='round',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='exam.Round'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='examiner',
            name='subject',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='exam.Subject'),
            preserve_default=False,
        ),
    ]
