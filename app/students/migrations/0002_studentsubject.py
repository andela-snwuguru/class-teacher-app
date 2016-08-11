# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-08-11 15:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('subject', '0003_auto_20160811_1624'),
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Student')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='subject.Subject')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
