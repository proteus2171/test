# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mobtick', '0003_auto_20150924_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='timestamp',
            field=models.DateField(auto_now_add=True),
        ),
    ]
