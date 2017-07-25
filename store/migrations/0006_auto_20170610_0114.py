# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_auto_20170609_1748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entry',
            old_name='date_created',
            new_name='datetime_created',
        ),
    ]
