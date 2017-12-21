from django.contrib import admin
from StudyDjango.models import Event, Guest


# Register your models here.
# 在此 注册你的数据模型
class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'start_time']
    search_fields = ['name']
    list_filter = ['status']

class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    search_fields = ['realname', 'phone']  # 搜索栏
    list_filter = ['sign']  # 过滤栏


admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)