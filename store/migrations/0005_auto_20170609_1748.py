# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_auto_20170609_1741'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='shop_url',
            field=models.URLField(max_length=512, unique=True, blank=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='brief',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='item_url',
            field=models.URLField(max_length=512, null=True),
        ),
    ]
