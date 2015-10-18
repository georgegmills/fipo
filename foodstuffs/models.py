from django.db import models

# Create your models here.

class Resource(models.Model):
    name = models.CharField(max_length=200)
    nut_free = models.BooleanField(default=false)
    lactose_free = models.BooleanField(default=false)
    gluten_free = models.BooleanField(default=false)

    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=200)
    resources = models.ManyToManyField(Resource)

    def is_nut_free(self):
        for resource in self.resources.all():
            if !resource.nut_free:
                return false
        return true

    def is_lactose_free(self):
        for resource in self.resources.all():
            if !resource.lactose_free:
                return false
        return true

    def is_gluten_free(self):
        for resource in self.resources.all():
            if !resource.gluten_free:
                return false
        return true

    def __str__(self):
        return self.name
    
class Menu(models.Model):
    name = models.CharField(max_length=200)
    meals = models.ManyToManyField(Meal)

    def is_nut_free(self):
        for meal in self.meals.all():
            if !meal.is_nut_free()
                return false
        return true

    def is_lactose_free(self):
        for meal in self.meals.all():
            if !meal.is_lactose_free():
                return false
        return true

    def is_gluten_free(self):
        for meal in self.meals.all():
            if !meal.is_gluten_free():
                return false
        return true

    def __str__(self):
        return self.name

class Trip(models.Model):
    name = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu)
    
    def __str__(self):
        return self.name
