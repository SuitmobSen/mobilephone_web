from django.contrib import admin
from .models import NewsList
# Register your models here.


class NewsListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', "description", "content")
    list_display_links = ('title', )
    search_fields = ('title', 'author', "description")


admin.site.register(NewsList, NewsListAdmin)
