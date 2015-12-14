# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20151213_2243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='owner',
            field=models.ForeignKey(related_name='snippets', default='', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
