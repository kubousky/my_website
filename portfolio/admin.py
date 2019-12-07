from django.contrib import admin
from .models import Category, Project, Img



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created', 'updated']
    list_filter = ['created', 'updated']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Img)
class ImgAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']