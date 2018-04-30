# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image_height',
            field=models.PositiveIntegerField(default=b'100', null=True, editable=False, blank=True),
        ),
        migrations.AddField(
            model_name='news',
            name='image_width',
            field=models.PositiveIntegerField(default=b'100', null=True, editable=False, blank=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(help_text=b'\xe8\xaf\xb7\xe4\xb8\x8a\xe4\xbc\xa0 344*244 \xe5\x83\x8f\xe7\xb4\xa0\xe7\x9a\x84\xe5\x9b\xbe\xe7\x89\x87', upload_to=b'news'),
        ),
    ]
