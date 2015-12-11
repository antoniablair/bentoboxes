# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='Recipe',
            field=models.ManyToManyField(related_name='liked_recipes', to='recipes.Recipe'),
        ),
    ]
