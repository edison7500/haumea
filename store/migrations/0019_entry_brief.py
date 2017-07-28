# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0018_remove_shop_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='brief',
            field=models.TextField(default=''),
        ),
    ]
