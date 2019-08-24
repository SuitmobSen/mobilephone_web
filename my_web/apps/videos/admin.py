from django.contrib import admin

# Register your models here.
from .models import Author, Tag, VideoList


class VideoListAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', "play", "duration", "make_time")
    list_display_links = ('title',)
    search_fields = ('title', 'author__name', "play", "duration", "make_time")


admin.site.register(Author)
admin.site.register(Tag)
admin.site.register(VideoList, VideoListAdmin)