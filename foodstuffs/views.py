from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404,render, render_to_response
from django import forms
from django.contrib import messages
from django.utils.translation import ugettext as _
from django.views import generic 

from .models import Resource, Unit, Allergen, Meal, MealTime, Menu
from .models import MealResourceRelationship,MenuMealRelationship,Trip
from .forms import MealForm, ResourceForm
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
    MealResourceFormset = forms.inlineformset_factory(Meal, Meal.resources.through, exclude=[], extra=0)
    
    if pk:
        meal = get_object_or_404(Meal, pk=pk)
    else:
        meal = Meal()
    
    # on POST, save
    if request.POST:
       meal_form = MealForm(request.POST, instance=meal)
       resource_formset = MealResourceFormset(request.POST, instance=meal)
       if meal_form.is_valid() and resource_formset.is_valid():
           # save first w/ commit=false, then normal save to avoid saving m2m
           # See: https://docs.djangoproject.com/en/1.8/topics/forms/modelforms/#the-save-method
           meal_mod = meal_form.save(commit=False)
           meal_mod.save()
                  
           # save resources
           resource_formset.save()
           
           
           messages.add_message(request, messages.SUCCESS, _('Meal correctly saved.'))
           
           # If the save was successful, redirect to another page
           redirect_url = reverse('meal_list')
           return HttpResponseRedirect(redirect_url)
    else:
        meal_form = MealForm(instance=meal)
        resource_formset = MealResourceFormset(instance=meal)
    
    args = {}
    args.update(csrf(request))
    args['form'] = meal_form
    args['formset'] = resource_formset
    args['meal'] = meal
    return render_to_response(template_name, args)
    


class ResourceView(generic.ListView):
    def get_queryset(self):
        return Resource.objects.all()    

class ResourceDetailView(generic.DetailView):
    model=Resource
    template_name = 'foodstuffs/resource_detail.html'

def resource_edit(request, pk=None,template_name='foodstuffs/resource_edit.html'):
    if pk:
        resource = get_object_or_404(Resource, pk=pk)
    else:
        resource = Resource()


    # on Post, save
    
    if request.POST:
        resource_form = ResourceForm(request.POST, instance=resource)
        if resource_form.is_valid():
            resource_mod = resource_form.save(commit=False)
            resource_mod.save()
            resource_form.save_m2m()

            redirect_url = reverse('resource_list')
            return HttpResponseRedirect(redirect_url)
    else:
        resource_form = ResourceForm(instance=resource)

    args = {}
    args.update(csrf(request))
    args['form'] = resource_form
    args['resource'] = resource
    return render_to_response(template_name, args)
