# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0008_auto_20151210_0014'),
    ]

    operations = [
        migrations.AlterField(
            model_name='like',
            name='recipe',
            field=models.ForeignKey(related_name='likes', to='recipes.Recipe'),
        ),
    ]
