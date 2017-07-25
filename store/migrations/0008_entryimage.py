# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_entry_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='EntryImage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('image', models.ImageField(verbose_name='Goods Picture', upload_to='images/')),
                ('entry', models.ForeignKey(related_name='images', to='store.Entry')),
            ],
        ),
    ]
