# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidapp', '0005_auto_20151015_1404'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cases',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('image', models.ImageField(help_text=b'\xe8\xaf\xb7\xe4\xb8\x8a\xe4\xbc\xa0 381*270 \xe5\x83\x8f\xe7\xb4\xa0\xe7\x9a\x84\xe5\x9b\xbe\xe7\x89\x87', upload_to=b'news', verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe5\x9b\xbe\xe7\x89\x87')),
                ('description1', models.TextField(verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe9\x9c\x80\xe6\xb1\x82')),
                ('description2', models.TextField(verbose_name=b'\xe8\xa7\xa3\xe5\x86\xb3\xe6\x96\xb9\xe6\xa1\x88')),
                ('description3', models.TextField(verbose_name=b'\xe6\x88\x90\xe7\xbb\xa9\xe5\xbd\xb1\xe5\x93\x8d')),
                ('pub_date', models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f')),
                ('description4', models.TextField(verbose_name=b'\xe6\x9c\x8d\xe5\x8a\xa1\xe5\x86\x85\xe5\xae\xb9')),
                ('description5', models.TextField(verbose_name=b'\xe5\xae\xa2\xe6\x88\xb7\xe5\x90\x8d\xe7\xa7\xb0')),
                ('description6', models.TextField(verbose_name=b'\xe9\x93\xbe\xe6\x8e\xa5')),
                ('news_category', models.CharField(default=b'uiux', max_length=8, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x88\x86\xe7\xb1\xbb', choices=[(b'uiux', b'UIUX'), (b'application', b'\xe5\xba\x94\xe7\x94\xa8\xe7\xa8\x8b\xe5\xba\x8f'), (b'website_design', b'\xe7\xbd\x91\xe7\xab\x99\xe8\xae\xbe\xe8\xae\xa1')])),
            ],
        ),
    ]
