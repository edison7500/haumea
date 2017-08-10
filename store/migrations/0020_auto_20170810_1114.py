# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0019_entry_brief'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='shop',
            name='shop_url',
            field=models.CharField(max_length=255, unique=True, blank=True),
        ),
    ]
