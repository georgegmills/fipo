from django.shortcuts import get_object_or_404,render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Resource, Unit, Allergen, Meal, MealTime, Menu
from .models import MealResourceRelationship,MenuMealRelationship,Trip
from django.views import generic 
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from .forms import MealForm
from django import forms
import logging

logger = logging.getLogger(__name__)

def index(request):
    return render(request,'foodstuffs/index.html')

class MealView(generic.ListView):
    def get_queryset(self):
        return Meal.objects.all()    

class MealDetailView(generic.DetailView):
    model = Meal
    template_name = 'foodstuffs/meal_detail.html'
    
# Form Views
# http://wiki.ddenis.com/index.php?title=Django,_add_and_edit_object_together_in_the_same_form
def meal_edit(request, pk=None, template_name='foodstuffs/meal_edit.html'):
    # ADDED: Created an inline formset factory for the meal resource relationship
    MealResourceFormset = forms.inlineformset_factory(Meal, Meal.resources.through, exclude=[], extra=1)

    if id:
        meal = get_object_or_404(Meal, pk=pk)
    else:
        meal = Meal()

    if request.POST:
       meal_form = MealForm(request.POST, instance=meal)
       resource_formset = MealResourceFormset(request.POST, request.FILES, instance=meal)

       if meal_form.is_valid() and resource_formset.is_valid():
            meal_mod = meal_form.save(commit=False)
            meal_mod.save()
            resource_formset.save()
            

                #messages.add_message(request, messages.SUCCESS, _('Meal correctly saved.'))            
            
            # If the save was successful, redirect to another page                                   
            redirect_url = reverse('meal_list')
            return HttpResponseRedirect(redirect_url)
    else:
        # ADDED/EDITED: create both the meal form and resource formsets
        meal_form = MealForm(instance=meal)
        resource_form = MealResourceFormset(instance=meal)                                                         

    args = {}
    args.update(csrf(request))
    args['form'] = meal_form
    args['formset'] = resource_formset
    args['meal'] = meal
    return render_to_response(template_name, args)
    
