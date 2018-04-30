# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidapp', '0008_auto_20151016_1453'),
    ]

    operations = [
        migrations.AddField(
            model_name='cases',
            name='title2',
            field=models.CharField(default='webdesign', max_length=128, verbose_name=b'\xe5\x89\xaf\xe6\xa0\x87\xe9\xa2\x98'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cases',
            name='image',
            field=models.ImageField(help_text=b'\xe8\xaf\xb7\xe4\xb8\x8a\xe4\xbc\xa0 380*270 \xe5\x83\x8f\xe7\xb4\xa0\xe7\x9a\x84\xe5\x9b\xbe\xe7\x89\x87', upload_to=b'cases', verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='cases',
            name='news_category',
            field=models.CharField(default=b'uiux', max_length=14, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x88\x86\xe7\xb1\xbb', choices=[(b'uiux', b'UIUX'), (b'application', b'\xe5\xba\x94\xe7\x94\xa8\xe7\xa8\x8b\xe5\xba\x8f'), (b'website_design', b'\xe7\xbd\x91\xe7\xab\x99\xe8\xae\xbe\xe8\xae\xa1')]),
        ),
    ]
