# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_auto_20151209_2322'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='likes',
        ),
        migrations.RemoveField(
            model_name='like',
            name='recipe',
        ),
        migrations.AddField(
            model_name='like',
            name='recipe',
            field=models.ForeignKey(default=0, to='recipes.Recipe'),
            preserve_default=False,
        ),
    ]
