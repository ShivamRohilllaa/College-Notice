from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(branch)
@admin.register(notice)
class noticeAdmin(admin.ModelAdmin):
    list_display = ['notice_id','subject', 'branch', 'cr_date']
    search_fields = ['subject', 'msg', 'branch']
    list_filter = ['branch', 'cr_date']

