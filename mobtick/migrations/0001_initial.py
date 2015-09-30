# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ticket',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('tech', models.CharField(max_length=50)),
                ('site', models.CharField(max_length=50)),
                ('user', models.CharField(max_length=50)),
                ('issue', models.CharField(max_length=200)),
                ('tickid', models.SmallIntegerField()),
                ('complete', models.BooleanField()),
                ('reqact', models.CharField(max_length=200, blank=True)),
            ],
            options={
                'verbose_name': 'MODELNAME',
                'verbose_name_plural': 'MODELNAMEs',
            },
        ),
    ]
