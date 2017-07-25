# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_auto_20170707_2114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': '商店', 'verbose_name_plural': '商店'},
        ),
        migrations.AlterField(
            model_name='entry',
            name='url',
            field=models.URLField(max_length=255, unique=True, null=True),
        ),
        migrations.AlterField(
            model_name='entryimage',
            name='image',
            field=models.URLField(max_length=255, editable=False),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_url',
            field=models.URLField(max_length=255, unique=True, blank=True),
        ),
    ]
