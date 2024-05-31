from django.contrib import admin
import djangoIntro.models as models


@admin.register(models.User)
class UserAdmin(admin.ModelAdmin):
    fields = ['first_name', 'last_name', 'email', 'age']
    list_display = ['first_name', 'last_name', 'email']
    search_fields = ['first_name', 'email']


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    fields = ['name']
    list_display = ['name']
    search_fields = ['name']

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    fields = ['name', 'description', 'category', 'price']
    list_display = ['name', 'price']
    search_fields = ['name', 'description']
