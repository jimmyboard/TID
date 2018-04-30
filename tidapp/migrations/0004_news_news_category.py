# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidapp', '0003_auto_20151012_0045'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='news_category',
            field=models.CharField(default=b'design', max_length=2, choices=[(b'design', b'\xe8\xae\xbe\xe8\xae\xa1'), (b'internet', b'\xe4\xba\x92\xe8\x81\x94\xe7\xbd\x91')]),
        ),
    ]
