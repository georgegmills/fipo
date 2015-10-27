# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Allergen',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MealResourceRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('units_per_person', models.DecimalField(max_digits=19, decimal_places=2)),
                ('meal', models.ForeignKey(to='foodstuffs.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='MealTime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='MenuMealRelationship',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('day', models.PositiveSmallIntegerField()),
                ('meal', models.ForeignKey(to='foodstuffs.Meal')),
                ('meal_time', models.ForeignKey(to='foodstuffs.MealTime')),
                ('menu', models.ForeignKey(to='foodstuffs.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('units_per_pack', models.PositiveSmallIntegerField()),
                ('packs_per_case', models.PositiveSmallIntegerField()),
                ('allergens', models.ManyToManyField(to='foodstuffs.Allergen')),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('menu', models.ForeignKey(to='foodstuffs.Menu')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='resource',
            name='unit',
            field=models.ForeignKey(to='foodstuffs.Unit'),
        ),
        migrations.AddField(
            model_name='menu',
            name='meals',
            field=models.ManyToManyField(to='foodstuffs.Meal', through='foodstuffs.MenuMealRelationship'),
        ),
        migrations.AddField(
            model_name='mealresourcerelationship',
            name='resource',
            field=models.ForeignKey(to='foodstuffs.Resource'),
        ),
        migrations.AddField(
            model_name='meal',
            name='resources',
            field=models.ManyToManyField(to='foodstuffs.Resource', through='foodstuffs.MealResourceRelationship'),
        ),
    ]
