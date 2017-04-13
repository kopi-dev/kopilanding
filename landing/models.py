from django.db import models
#from django.db.models.signals import pre_save


class Page(models.Model):
    page_name = models.CharField('Назыание страницы', max_length=200)
    # NavBar
    project_name = models.CharField('Название проекта', default='My Landing Page', max_length=40)
    phone = models.CharField('Телефон', default='+7 000 000-00-00', max_length=20)
    mail = models.EmailField('E-mail', default='info@domen.com')

    # Main
    title = models.CharField('Заголовок', max_length=200)
    sub_title = models.CharField('Подзаголовок', max_length=200, blank=True, null=True)
    title_btn = models.CharField('Текст кнопки', max_length=50, default='Действие')
    title_btn_url = models.CharField('URL кнопки', max_length=50, blank=True, null=True)
    background_color = models.CharField('Цвет фона', default='#5180a5', max_length=7, blank=True, null=True)

    # Footer
    #footer_content = models.TextField('Подвал', blank=True, null=True)
    address = models.CharField('Адрес', max_length=250, blank=True, null=True)


    def __str__(self):
        return self.page_name

    class Meta:
        verbose_name = 'Страница проекта'
        verbose_name_plural = 'Страницы проекта'


class MainReasonToBelieve(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    text = models.CharField('Текст под заголовком', max_length=100, blank=True, null=True)

    def __str__(self):
        return ''


class Process(models.Model):
    page = models.ForeignKey(Page, on_delete=models.CASCADE)
    title = models.CharField('Заголовок', max_length=150, blank=True, null=True)
    sub_title = models.CharField('Подзаголовок', max_length=150, blank=True, null=True)
    content = models.TextField('Блок', blank=True, null=True)
    img_path = models.TextField('Ссылки на изображения (каждую с новой строки)', blank=True, null=True)

    def img_path_as_list(self):
        return str(self.img_path).split()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Процесс'
        verbose_name_plural = 'Процесс'


class Document(models.Model):
    name = models.CharField('Ваше имя', blank=True, null=True, max_length=25)
    phone = models.CharField('Телефон для связи', max_length=20)
    email = models.EmailField('E-mail', blank=True, null=True)
    description = models.TextField('Комментарий к заказу', max_length=500, blank=True, null=True)
    document = models.FileField('Прикрепить файл', upload_to='documents/', blank=True, null=True)
    uploaded_at = models.DateTimeField('Создан', auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ на расчет'
        verbose_name_plural = 'Заявка на расчет'

    def __str__(self):
        return self.email
