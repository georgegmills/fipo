from django.db import models

# Create your models here.

class Alergen(models.Model):
    name= models.CharField(max_length=200)

class Resource(models.Model):
    name = models.CharField(max_length=200)
    alergens = models.ManyToManyField(Alergen)
    
    def __str__(self):
        return self.name

class Meal(models.Model):
    name = models.CharField(max_length=200)
    resources = models.ManyToManyField(Resource)

    def get_alergens(self):
        alergens = []
        for resource in self.resources.all():
            alergens.append(resource.alergens)
        return 
            



    def __str__(self):
        return self.name
    
class Menu(models.Model):
    name = models.CharField(max_length=200)
    meals = models.ManyToManyField(Meal)

    def get_meal_alergens(self):
        for meal in self.meals.all():

            #return all alergens associated in resource. Add them to a list? 



    def __str__(self):
        return self.name

class Trip(models.Model):
    name = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu)
    
    def __str__(self):
        return self.name
