from django.contrib import admin
from .models import Allergen, Unit, Resource, Meal, MealResourceRelationship, MealTime, Menu, MenuMealRelationship, Trip
# Register your models here.

class AllergenAdmin(admin.ModelAdmin):
    fields = ['name']

class MealResourceInline(admin.TabularInline):
    model = MealResourceRelationship
    extra = 1

class MealAdmin(admin.ModelAdmin):
    inlines = (MealResourceInline,)

class MenuMealInline(admin.TabularInline):
    model = MenuMealRelationship
    extra = 1

class MenuAdmin(admin.ModelAdmin):
    inlines = (MenuMealInline,)

admin.site.register(Allergen, AllergenAdmin)
admin.site.register(Unit)
admin.site.register(Resource)
admin.site.register(Meal,MealAdmin)
admin.site.register(MealTime)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Trip)


