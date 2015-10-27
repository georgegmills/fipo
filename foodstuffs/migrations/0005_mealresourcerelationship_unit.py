# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodstuffs', '0004_auto_20151020_2301'),
    ]

    operations = [
        migrations.AddField(
            model_name='mealresourcerelationship',
            name='unit',
            field=models.ForeignKey(default=b'', to='foodstuffs.Unit'),
        ),
    ]
