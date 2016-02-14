# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lunches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lunch',
            name='foods',
            field=models.ManyToManyField(related_name='lunches', to='lunches.Food'),
        ),
    ]
