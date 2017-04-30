# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-29 18:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_auto_20170429_1815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobsinfo',
            name='description',
            field=models.CharField(default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobsinfo',
            name='job_type',
            field=models.CharField(choices=[('fulltime', 'FULLTIME'), ('parttime', 'PARTTIME'), ('remote', 'REMOTE'), ('internship', 'INTERNSHIP')], default='FULL TIME', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobsinfo',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobsinfo',
            name='skill',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='jobsinfo',
            name='wage',
            field=models.CharField(choices=[('< 5.000.000', '< 5.000.000'), ('5.000.000 -> 10.000.000', '5.000.000 -> 10.000.000'), ('10.000.000 -> 15.000.000', '10.000.000 -> 15.000.000'), ('15.000.000 -> 20.000.000', '15.000.000 -> 20.000.000'), ('20.000.000 -> 25.000.000', '20.000.000 -> 25.000.000'), ('25.000.000 -> 30.000.000', '25.000.000 -> 30.000.000'), ('> 30.000.000', '> 30.000.000')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='jobsinfo',
            name='welfare',
            field=models.TextField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='jobsinfo',
            name='work',
            field=models.TextField(max_length=250, null=True),
        ),
    ]
