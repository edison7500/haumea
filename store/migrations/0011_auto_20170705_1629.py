# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20170628_1623'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='entrystat',
            unique_together=set([('entry', 'date_created')]),
        ),
    ]
