# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=128)),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('views', models.IntegerField(default=0)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=b'news')),
            ],
        ),
    ]
