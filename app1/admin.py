from django.contrib import admin
from django.utils.html import format_html
from .models import Customer, Product, Category

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'address')
    search_fields = ('first_name', 'last_name', 'email', 'phone_number', 'address')
    list_filter = ('first_name', 'last_name',) 

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'unit', 'display_image', 'category')
    list_filter = ('category',)
    search_fields = ('name', 'category__name')

    def display_image(self, obj):
        if obj.image: 
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return None

    display_image.short_description = 'Image'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','display_image', 'date_added', 'date_created')
    search_fields = ('name',)
    def display_image(self, obj):
        if obj.image: 
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return None

    display_image.short_description = 'Image'

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
