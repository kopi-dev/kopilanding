from django.contrib import admin

from .models import Page, MainReasonToBelieve, Process
# Register your models here.


class MainReasonToBelieveInline(admin.StackedInline):
    model = MainReasonToBelieve
    #extra = 3


class ProcessInline(admin.StackedInline):
    model = Process


class PageAdmin(admin.ModelAdmin):
    #fieldsets = [
    #    (None,               {'fields': ['question_text']}),
    #    ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    #]
    inlines = [MainReasonToBelieveInline, ProcessInline]


admin.site.register(Page, PageAdmin)
