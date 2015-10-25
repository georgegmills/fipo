from django.shortcuts import get_object_or_404,render, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from .models import Resource, Unit, Allergen, Meal, MealTime, Menu
from .models import MealResourceRelationship,MenuMealRelationship,Trip
from django.views import generic 
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf
from .forms import MealForm


def index(request):
    return render(request,'foodstuffs/index.html')

class MealView(generic.ListView):
    template_name = 'foodstuffs/meals_list.html'
    context_object_name = 'meals_list'
    
    def get_queryset(self):
        return Meal.objects.all()    


class MealDetailView(generic.DetailView):
    model = Meal
    template_name = 'foodstuffs/meal_detail.html'
    
#Form Views

def create_meal(request):
    if request.POST:
        form = MealForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('meals_list'))

    else:
        form = MealForm()

    args = {}
    args.update(csrf(request))

    args['form'] = form

    return render_to_response('foodstuffs/create_meal.html', args)
    
