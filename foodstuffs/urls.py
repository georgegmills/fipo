from django.conf.urls import url

from . import views

urlpatterns = [ 
    url(r'^$', views.index, name='index'),
    url(r'^meals/add$', views.meal_edit, name='meal_add'),
    url(r'^meals/(?P<pk>\d+)/edit$', views.meal_edit, name='meal_edit'),
    url(r'^meals/(?P<pk>\d+)/view$', views.MealDetailView.as_view(), name='meal_detail'),
    url(r'^meals$', views.MealView.as_view(), name='meal_list'),

    url(r'^resources/add$', views.resource_edit, name='resource_add'),
    url(r'^resources/(?P<pk>\d+)/edit$', views.resource_edit, name='resource_edit'),
    url(r'^resources/(?P<pk>\d+)/view$', views.ResourceDetailView.as_view(), name='resource_detail'),
    url(r'^resources$', views.ResourceView.as_view(), name='resource_list'),
]
