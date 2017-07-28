# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0017_auto_20170728_1714'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shop',
            name='slug',
        ),
    ]
