# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidapp', '0009_auto_20151016_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cases',
            name='description4',
            field=models.CharField(max_length=128, verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='description5',
            field=models.CharField(max_length=128, verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='description6',
            field=models.CharField(max_length=128, verbose_name=b'\xe7\xbd\x91\xe7\xab\x99\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
    ]
