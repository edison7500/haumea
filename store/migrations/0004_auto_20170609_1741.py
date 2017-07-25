# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_entry_date_created'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entrystat',
            old_name='create_datetime',
            new_name='date_created',
        ),
    ]
