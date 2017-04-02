from django.shortcuts import render
from django.views.generic import View, TemplateView
from landing.models import *

class LandingView(TemplateView):

    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super(LandingView, self).get_context_data(**kwargs)
        context['page_obj'] = Page.objects.all().order_by("?").first()
        context['reas_to_bel_obj'] = MainReasonToBelieve.objects.all()
        context['process_obj'] = Process.objects.all()


        return context
