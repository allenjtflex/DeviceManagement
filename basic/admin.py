from django.contrib import admin
from .models import Category, Equipment

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
	list_display = ['id', 'category', 'brand','description','spec']

class EquipmentAdmin(admin.ModelAdmin):
	list_display = ['id', 'category', 'brand','description','spec', 'create_at']
	ordering = ['id']


admin.site.register(Category)
admin.site.register(Equipment, EquipmentAdmin)