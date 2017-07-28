# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_shop_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop',
            name='slug',
            field=django_extensions.db.fields.RandomCharField(blank=True, editable=False, length=12, include_alpha=False),
        ),
    ]
