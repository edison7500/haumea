# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20170618_2043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrystat',
            options={'ordering': ['date_created']},
        ),
        migrations.AlterField(
            model_name='entryimage',
            name='image',
            field=models.URLField(max_length=512, editable=False),
        ),
    ]
