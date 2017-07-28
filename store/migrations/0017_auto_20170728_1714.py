# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20170728_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='slug',
            field=django_extensions.db.fields.RandomCharField(blank=True, db_index=True, editable=False, length=12, include_alpha=False),
        ),
    ]
