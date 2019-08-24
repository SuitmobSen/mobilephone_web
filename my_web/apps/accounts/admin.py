from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'mobile', 'qq', 'is_staff', 'last_login')
    list_display_links = ('username',)
    search_fields = ('username', 'email', 'mobile', 'qq')


admin.site.register(User, UserAdmin)


