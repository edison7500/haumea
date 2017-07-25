# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20170606_0655'),
    ]

    operations = [
        migrations.AddField(
            model_name='entry',
            name='date_created',
            field=models.DateTimeField(db_index=True, default=django.utils.timezone.now),
        ),
    ]
