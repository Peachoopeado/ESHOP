from django.contrib import admin
from .models import Category, Product, OilType, Viscosity, Compound, Fuel, Transmission


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class OilTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(OilType, OilTypeAdmin)


class ViscosityAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Viscosity, ViscosityAdmin)

class CompoundAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Compound, CompoundAdmin)

class TransmissionAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Transmission, TransmissionAdmin)
class FuelAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Fuel, FuelAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'oilType', 'viscosity', 'compound', 'fuel', 'price', 'stock', 'available', 'created', 'updated']
    list_filter = ['available', 'created', 'updated', 'oilType', 'viscosity', 'compound', 'fuel']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Product, ProductAdmin)
