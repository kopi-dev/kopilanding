from django.db import models
from django.db.models.signals import pre_save


class Page(models.Model):

    project_name      = models.CharField('Название проекта', max_length=40)
    title             = models.CharField('Заголовок', max_length=200)
    title_description = models.TextField('Текст под заголовком', blank=True, null=True)
    title_btn         = models.CharField('Текст кнопки', max_length=50, default='Learn')
    title_btn_url     = models.CharField('URL кнопки', max_length=50, blank=True, null=True)
    content           = models.TextField('Контент', blank=True, null=True)

    def __str__(self):
        return self.title
