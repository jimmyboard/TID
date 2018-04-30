# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidapp', '0002_auto_20151012_0041'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='image_height',
        ),
        migrations.RemoveField(
            model_name='news',
            name='image_width',
        ),
    ]
