from django import forms
from django.forms import  inlineformset_factory
from .models import MealResourceRelationship, Meal, Resource

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = '__all__'

   

