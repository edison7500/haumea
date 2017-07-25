# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_auto_20170610_0114'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='url',
            field=models.URLField(max_length=512, null=True),
        ),
    ]
