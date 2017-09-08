from django.contrib import admin
from StudyDjango.models import Event, Guest


# Register your models here.

class EventAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'status', 'address', 'start_time']


class GuestAdmin(admin.ModelAdmin):
    list_display = ['realname', 'phone', 'email', 'sign', 'create_time', 'event']
    search_fields = ['realname', 'phone']  # 搜索栏
    list_filter = ['sign']  # 过滤栏

admin.site.register(Event, EventAdmin)
admin.site.register(Guest, GuestAdmin)

