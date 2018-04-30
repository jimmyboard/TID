# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tidapp', '0004_news_news_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128, verbose_name=b'\xe5\x90\x8d\xe5\xad\x97')),
                ('tel', models.CharField(max_length=128, verbose_name=b'\xe8\x81\x94\xe7\xb3\xbb\xe7\x94\xb5\xe8\xaf\x9d')),
                ('content', models.TextField(verbose_name=b'\xe9\x9c\x80\xe6\xb1\x82')),
            ],
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(verbose_name=b'\xe5\x86\x85\xe5\xae\xb9'),
        ),
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(help_text=b'\xe8\xaf\xb7\xe4\xb8\x8a\xe4\xbc\xa0 344*244 \xe5\x83\x8f\xe7\xb4\xa0\xe7\x9a\x84\xe5\x9b\xbe\xe7\x89\x87', upload_to=b'news', verbose_name=b'\xe4\xb8\x8a\xe4\xbc\xa0\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_category',
            field=models.CharField(default=b'design', max_length=8, verbose_name=b'\xe6\x96\x87\xe7\xab\xa0\xe5\x88\x86\xe7\xb1\xbb', choices=[(b'design', b'\xe8\xae\xbe\xe8\xae\xa1'), (b'internet', b'\xe4\xba\x92\xe8\x81\x94\xe7\xbd\x91')]),
        ),
        migrations.AlterField(
            model_name='news',
            name='pub_date',
            field=models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xa5\xe6\x9c\x9f'),
        ),
        migrations.AlterField(
            model_name='news',
            name='title',
            field=models.CharField(max_length=128, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0, verbose_name=b'\xe6\xb5\x8f\xe8\xa7\x88\xe6\xac\xa1\xe6\x95\xb0'),
        ),
    ]
