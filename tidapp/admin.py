from django.contrib import admin
from .models import News, Advisory, Cases

# Register your models here.

class CasesAdmin(admin.ModelAdmin):
    list_display = ('title', 'title2', 'pub_date', 'description4', 'description5', 'description6')
    list_filter = ['pub_date']
    search_fields = ['title']

class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'views')
    list_filter = ['pub_date']
    search_fields = ['title']

class AdvisoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'tel', 'content')
    search_fields = ['name']

admin.site.register(News, NewsAdmin)
admin.site.register(Advisory, AdvisoryAdmin)
admin.site.register(Cases, CasesAdmin)