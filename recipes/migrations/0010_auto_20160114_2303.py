# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0009_auto_20151210_0040'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('creator', models.ManyToManyField(related_name='labels', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='category',
            name='recipes',
            field=models.ManyToManyField(related_name='categories', to='recipes.Recipe'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', to='recipes.Ingredient'),
        ),
        migrations.AddField(
            model_name='label',
            name='recipes',
            field=models.ManyToManyField(to='recipes.Recipe'),
        ),
    ]
