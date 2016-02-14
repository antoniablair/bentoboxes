# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='city',
            field=models.TextField(max_length=200, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='occupation',
            field=models.TextField(max_length=300, blank=True),
        ),
        migrations.AddField(
            model_name='member',
            name='state',
            field=models.TextField(max_length=200, blank=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='avatar',
            field=models.ImageField(upload_to=b'images/'),
        ),
    ]
