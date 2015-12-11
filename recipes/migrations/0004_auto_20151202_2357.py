# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='text',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='measurement',
            field=models.CharField(default=b'pinch', max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='ingredient',
            name='quantity',
            field=models.DecimalField(default=b'1', null=True, max_digits=5, decimal_places=2, blank=True),
        ),
    ]
