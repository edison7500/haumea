# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_entryimage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrystat',
            options={'ordering': ['-date_created']},
        ),
        migrations.AlterField(
            model_name='entry',
            name='url',
            field=models.URLField(max_length=512, unique=True, null=True),
        ),
    ]
