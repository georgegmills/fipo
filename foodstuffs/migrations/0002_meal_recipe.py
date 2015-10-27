# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodstuffs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meal',
            name='recipe',
            field=models.TextField(default=b''),
        ),
    ]
