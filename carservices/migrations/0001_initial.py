# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-29 13:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('carmeid', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('token', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.CharField(max_length=200)),
                ('latitude', models.CharField(max_length=200)),
                ('bearing', models.CharField(max_length=200)),
                ('speed', models.CharField(max_length=200)),
                ('time', models.DateTimeField()),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carservices.Account')),
            ],
        ),
        migrations.CreateModel(
            name='WXUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('openid', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('head_portrait', models.URLField()),
                ('bind', models.BooleanField()),
                ('account', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='carservices.Account')),
            ],
        ),
    ]
