from django.contrib import admin

from .models import Page, MainReasonToBelieve, Process, Document


class MainReasonToBelieveInline(admin.TabularInline):
    model = MainReasonToBelieve
    fieldsets = [
        ('Пункты главного блока', {'fields': ['text']}),
    ]
    extra = 1


class ProcessInline(admin.StackedInline):
    model = Process
    fieldsets = [
        ('Процесс', {'fields': ['title', 'sub_title', 'content', 'img_path'], 'classes': ['collapse']})
    ]
    extra = 1


class PageAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Называние страницы', {'fields': ['page_name']}),
        ('Панель навигации',   {'fields': ['project_name', 'phone', 'mail']}),
        ('Главный блок',       {'fields': ['title', 'sub_title', 'title_btn', 'title_btn_url', 'background_color']}),
        ('Адрес',             {'fields': ['address'], 'classes': ['collapse']}),
        ('Политика', {'fields': ['privacy']}),
    ]
    inlines = [MainReasonToBelieveInline, ProcessInline]


class DocumentAdmin(admin.ModelAdmin):
    list_display = ["pk", "phone", "email", "document", "uploaded_at"]

admin.site.register(Page, PageAdmin)
admin.site.register(Document, DocumentAdmin)
