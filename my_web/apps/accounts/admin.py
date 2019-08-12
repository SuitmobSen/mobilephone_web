from django.contrib import admin
from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'mobile', 'qq', 'is_active', 'last_login')
    search_fields = ('username', 'email', 'mobile', 'qq')


admin.site.register(User, UserAdmin)


