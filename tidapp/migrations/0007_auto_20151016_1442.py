# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidapp', '0006_cases'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='image2',
            field=models.ImageField(default=None, help_text=b'\xe8\xaf\xb7\xe4\xb8\x8a\xe4\xbc\xa0\xe5\xae\xbd\xe4\xb8\xba 1170 \xe5\x83\x8f\xe7\xb4\xa0\xe7\x9a\x84\xe5\x9b\xbe\xe7\x89\x87', verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe5\x9b\xbe\xe7\x89\x87', upload_to=b'news'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='description6',
            field=models.TextField(verbose_name=b'\xe7\xbd\x91\xe7\xab\x99\xe9\x93\xbe\xe6\x8e\xa5'),
        ),
    ]
