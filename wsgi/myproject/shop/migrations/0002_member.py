# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('username', models.CharField(max_length=16, serialize=False, primary_key=True)),
                ('password', models.CharField(max_length=16)),
                ('name', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=11)),
            ],
        ),
    ]
