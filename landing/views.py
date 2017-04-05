from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, FormView
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
            return redirect('landing')
