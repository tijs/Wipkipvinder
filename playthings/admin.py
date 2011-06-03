from django.contrib import admin
from playthings.models import Plaything, Hood, City, Country, Type, Category

admin.site.register(Plaything)
admin.site.register(Type)
admin.site.register(Category)
admin.site.register(Hood)
admin.site.register(City)
admin.site.register(Country)