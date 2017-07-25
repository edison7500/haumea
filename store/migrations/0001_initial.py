# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='EntryStat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('price', models.DecimalField(default=0, max_digits=10, decimal_places=2)),
                ('sale_num', models.IntegerField(default=0)),
                ('create_datetime', models.DateField(default=django.utils.timezone.now, db_index=True)),
                ('entry', models.ForeignKey(related_name='stat', to='store.Entry')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=128, blank=True)),
                ('brief', models.TextField()),
                ('type', models.CharField(max_length=32)),
                ('item_url', models.URLField(unique=True, max_length=512)),
                ('created_datetime', models.DateTimeField(default=django.utils.timezone.now, db_index=True)),
            ],
        ),
        migrations.AddField(
            model_name='entry',
            name='shop',
            field=models.ForeignKey(related_name='entry', to='store.Shop'),
        ),
    ]
