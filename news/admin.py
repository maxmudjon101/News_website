from django.contrib import admin
from .models import News,Comment,Category


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title','slug','category','status']
    list_filter = ['category','status']
    prepopulated_fields = {"slug": ('title',)}



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','name']

admin.site.register(News,NewsAdmin)
admin.site.register(Category)
