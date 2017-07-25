# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='type',
            field=models.SmallIntegerField(verbose_name='type', default=0, choices=[(0, 'tmall'), (1, 'taobao'), (2, 'jd')]),
        ),
    ]
