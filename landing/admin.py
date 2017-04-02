from django.contrib import admin

from .models import Page, MainReasonToBelieve, Process
# Register your models here.


class MainReasonToBelieveInline(admin.TabularInline):
    model = MainReasonToBelieve
    fieldsets = [
        ('Пункты главного блока', {'fields': ['text']}),
    ]
    extra = 1


class ProcessInline(admin.TabularInline):
    model = Process
    fieldsets = [
        ('Процесс', {'fields': ['title','sub_title','content','img_path'], 'classes': ['collapse']})
    ]
    extra = 1

class PageAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Называние страницы', {'fields': ['page_name']}),
        ('Панель навигации',   {'fields': ['project_name', 'phone']}),
        ('Главный блок',       {'fields': ['title', 'title_btn', 'title_btn_url', 'background_color']}),
        ('Подвал',             {'fields': ['footer_content'], 'classes': ['collapse']}),
    ]
    inlines = [MainReasonToBelieveInline, ProcessInline]


admin.site.register(Page, PageAdmin)
