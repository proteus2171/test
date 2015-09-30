# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobtick', '0002_auto_20150924_1254'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='id',
        ),
        migrations.AlterField(
            model_name='ticket',
            name='tickid',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
