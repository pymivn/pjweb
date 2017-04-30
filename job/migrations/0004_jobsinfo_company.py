# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-04-29 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companys', '0003_auto_20170429_1413'),
        ('job', '0003_remove_jobsinfo_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobsinfo',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='companys.CompanyProfile'),
        ),
    ]
