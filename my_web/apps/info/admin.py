from django.contrib import admin

# Register your models here.
from .models import Phone, PhoneModel, Params, BasicParams


class PhoneModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'brand', 'model', "basicparams")
    list_display_links = ('model',)
    search_fields = ('brand', 'model', "basicparams")


# 定制关联类（Params是外键）
class PhoneModelInLine(admin.StackedInline):
    model = PhoneModel
    extra = 0


# Params是外键，希望编辑Params是可以看到关联的类信息
class ParamsAdmin(admin.ModelAdmin):
    list_display = ("basic", "screen", 'hardware', 'net', 'camera', 'appearance', 'function', 'pack', 'protect')
    list_display_links = ('basic',)
    # inlines: 关联数据,如外键/m2m/o2o,Params是Entry的外键
    inlines = [PhoneModelInLine, ]


class BasicParamsAdmin(admin.ModelAdmin):
    list_display = ("cpu", "back", 'front', 'memory', 'battery', 'screen', "dpi")
    list_display_links = ("cpu",)
    # inlines: 关联数据,如外键/m2m/o2o,Params是Entry的外键
    inlines = [PhoneModelInLine, ]


admin.site.register(Phone)
admin.site.register(PhoneModel, PhoneModelAdmin)
admin.site.register(Params, ParamsAdmin)
admin.site.register(BasicParams, BasicParamsAdmin)
