from django.db import models
from sets import Set

# Create your models here.

class Allergen(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

# allow repeat of units rather than text field, easier interface
class Unit(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# a resource is a food item. e.g. "Bananas" 
# resources have a  unit specifies in what units 
# the resource is bought e.g. Bananas Unit = ct or count, water = gal 
class Resource(models.Model):
    name = models.CharField(max_length=200)
    unit = models.ForeignKey(Unit)
    units_per_pack = models.PositiveSmallIntegerField()
    packs_per_case = models.PositiveSmallIntegerField()
    allergens = models.ManyToManyField(Allergen, blank=True)

# has_allergen is a function that checks for 
# a specific allergen in a resource
    def has_allergen(self, allergen):
        for a in self.allergens.all():
            if a == allergen:
                return true
        return false
    
    def __str__(self):
        return self.name

# Meal is a collection of resources to make a particular 
# food dish i.e. Meal = Mac and Cheese, Resources = Cheese, pasta ... etc
class Meal(models.Model):
    name = models.CharField(max_length=200)
    resources = models.ManyToManyField(Resource, through='MealResourceRelationship')
    recipe = models.TextField(default='')

    def get_allergens(self):
        allergens = set()
        for resource in self.resources.all():
            allergens |= set(resource.allergens)
        return list(allergens)

    # fastest to look through one by one rather than using get_allergens
    # allows short-circuiting once found
    def has_allergen(self, allergen):
        for resource in self.resources.all():
            if resource.allergens.all().count(allergen) > 0:
                return true
        return false

    def __str__(self):
        return self.name

class MealResourceRelationship(models.Model):
    resource = models.ForeignKey(Resource)
    meal = models.ForeignKey(Meal)
    units_per_person = models.DecimalField(max_digits=19,decimal_places=2)

class MealTime(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    name = models.CharField(max_length=200)
    meals = models.ManyToManyField(Meal, through='MenuMealRelationship')

    def get_allergens(self):
        allergens = set()
        for meal in self.meals.all():
            allergens |= set(meal.get_allergens())
        return list(allergens)

    # fastest to look through one by one rather than using get_allergens
    # allows short-circuiting once found
    def has_allergen(self, allergen):
        for meal in self.meals.all():
            if meal.get_allergens().count(allergen) > 0:
                return true
        return false

    def __str__(self):
        return self.name


class MenuMealRelationship(models.Model):
    meal = models.ForeignKey(Meal)
    menu = models.ForeignKey(Menu)
    meal_time = models.ForeignKey(MealTime)
    day = models.PositiveSmallIntegerField()

class Trip(models.Model):
    name = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu)
    
    def __str__(self):
        return self.name
