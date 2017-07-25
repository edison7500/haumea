# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_auto_20170705_1629'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'verbose_name': 'Store', 'verbose_name_plural': 'Stores'},
        ),
        migrations.RemoveField(
            model_name='shop',
            name='item_url',
        ),
        migrations.AlterUniqueTogether(
            name='entrystat',
            unique_together=set([]),
        ),
    ]
