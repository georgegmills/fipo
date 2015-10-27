# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodstuffs', '0002_meal_recipe'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergen',
            name='name',
            field=models.CharField(max_length=200, blank=True),
        ),
    ]
