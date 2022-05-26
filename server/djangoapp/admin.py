from django.contrib import admin
from .models import *


# Register your models here.

# CarModelInline class
class CarModelInline(admin.StackedInline):
    model = CarModel
    extra = 3
# CarModelAdmin class
class CarModelAdmin(admin.ModelAdmin):
     model = CarModel
     list_display = ( 'name','dealer_id','type','year')
  
# CarMakeAdmin class with CarModelInline
class CarMakeAdmin(admin.ModelAdmin):
      model = CarMake
      list_display = ('name',)
     
     
      inlines = [CarModelInline]

# Register models here

admin.site.register(CarMake , CarMakeAdmin)
admin.site.register(CarModel , CarModelAdmin )

#admin.site.register(CarDealer)
#admin.site.register(DealerReview)