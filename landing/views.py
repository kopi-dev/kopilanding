from django.contrib import messages
from django.core.mail import send_mail
from kopilanding.settings import local
from django.views.generic import TemplateView, FormView


from landing.models import *

from .forms import DocumentForm


class LandingView(TemplateView, FormView):
    template_name = 'home.html'
    form_class = DocumentForm

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        context['page_obj'] = Page.objects.all().order_by("?").first()
        context['reas_to_bel_obj'] = MainReasonToBelieve.objects.all()
        context['process_obj'] = Process.objects.all()
        return context

    def form_valid(self, form):
        if form.is_valid():
            form.save()
            form_phone = form.cleaned_data.get('phone')
            form_email = form.cleaned_data.get('email')
            form_description = form.cleaned_data.get('description')
            doc_name = form.cleaned_data.get('document')
            subject = 'Новая заявка с лендинга'
            from_email = local.EMAIL_HOST_USER
            content = '''
            Телефон: {0}\n
            E-mail: {1}\n
            Описание: {2}\n
            Файл: {3}{4}'''.format(
                form_phone,
                form_email,
                form_description,
                local.PATH_TO_DOC,
                doc_name
            )

            send_mail(
                subject,
                content,
                from_email,
                local.to_email,
                fail_silently=False,
            )

            messages.add_message(self.request, messages.SUCCESS, 'Заявка успешно отправлена')

            try:
                from kopilanding.telegrambot import send_message
                send_message([subject, content])
            except: pass

            #return redirect('landing')
            return self.render_to_response(self.get_context_data())
