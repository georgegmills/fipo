# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodstuffs', '0003_auto_20151020_2255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='allergen',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='resource',
            name='allergens',
            field=models.ManyToManyField(to='foodstuffs.Allergen', blank=True),
        ),
    ]
