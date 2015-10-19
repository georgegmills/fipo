from django.db import models
from sets import Set

# Create your models here.

class Allergen(models.Model):
    name = models.CharField(max_length=200)

class Resource(models.Model):
    name = models.CharField(max_length=200)
    allergens = models.ManyToManyField(Allergen)

    def has_allergen(self, allergen):
        for a in self.allergens.all():
            if a == allergen:
                return true
        return false
    
    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=200)
    resources = models.ManyToManyField(Resource)

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
    
class Menu(models.Model):
    name = models.CharField(max_length=200)
    meals = models.ManyToManyField(Meal)

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

class Trip(models.Model):
    name = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu)
    
    def __str__(self):
        return self.name
