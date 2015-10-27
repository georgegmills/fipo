from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^$', views.index, name='index'),
    url(r'^meals_list.html/$', views.MealView.as_view(), name='meals_list'),
    url(r'^(?P<pk>[0-9]+)/detail$', views.MealDetailView.as_view(), name='meal_detail'),
    url(r'^create_meal/$', views.create_meal, name='create_meal'),
]
