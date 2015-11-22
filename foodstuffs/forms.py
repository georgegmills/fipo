from django import forms
from django.forms import  inlineformset_factory
from .models import MealResourceRelationship, Meal, Resource

class MealForm(forms.Form):
    model = Meal
    name = forms.CharField(max_length=200)
    resources = inlineformset_factory(Resource, Meal.resources.through, fields=('resource','units_per_person'))
    recipe = forms.CharField(max_length=2000)

   

