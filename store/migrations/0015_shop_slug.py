# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_auto_20170725_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='slug',
            field=django_extensions.db.fields.RandomCharField(unique=True, blank=True, editable=False, length=12, include_alpha=False),
        ),
    ]
