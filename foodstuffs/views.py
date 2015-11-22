from django.shortcuts import get_object_or_404,render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from .models import Resource, Unit, Allergen, Meal, MealTime, Menu
from .models import MealResourceRelationship,MenuMealRelationship,Trip
from django.views import generic 
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from .forms import MealForm
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
    if id:
        meal = get_object_or_404(Meal, pk=pk)
    else:
        meal = Meal()

    if request.POST:
       form = MealForm(request.POST,instance=meal)
       if form.is_valid():
            meal_mod = form.save(commit=False)
            meal_mod.save()
            
            # remove existing resources
            meal_mod.resources.clear()
            for resource in form.cleaned_data.get('resources'):
                meal_resource_rel = MealResourceRelationship(meal=meal_mod, 
                                                             resource=resource,
                                                             units_per_person=1)
                meal_resource_rel.save()
            # messages.add_message(request, messages.SUCCESS, _('Meal correctly saved.'))
            # If the save was successful, redirect to another page
            redirect_url = reverse('meal_list')
            return HttpResponseRedirect(redirect_url)
    else:
        form = MealForm(instance=meal)

    args = {}
    args.update(csrf(request))
    args['form'] = form
    args['meal'] = meal
    return render_to_response(template_name, args)
    
