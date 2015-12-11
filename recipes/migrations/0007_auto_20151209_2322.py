# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_like_recipe'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='Recipe',
            new_name='recipe',
        ),
    ]
