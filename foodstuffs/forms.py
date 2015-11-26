from django import forms
from .models import MealResourceRelationship, Meal

class MealForm(forms.ModelForm):
    class Meta:
        model = Meal
        fields = ['name', 'recipe']
        # resources should be handled by fieldset


