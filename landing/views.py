from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, FormView
from landing.models import *
from .forms import DocumentForm


class LandingView(TemplateView, FormView):
    template_name = 'home.html'

    form_class = DocumentForm

    def get_context_data(self, **kwargs):
        form = DocumentForm
        context = super(LandingView, self).get_context_data(**kwargs)
        context['page_obj'] = Page.objects.all().order_by("?").first()
        context['reas_to_bel_obj'] = MainReasonToBelieve.objects.all()
        context['process_obj'] = Process.objects.all()
        context['form'] = form

        return context

    def form_valid(self, form):
    # This method is called when valid form data has been POSTed.
    # It should return an HttpResponse.
        form.save()

        redirect('landing')
        #return super(DocumentForm, self).form_valid(form)
        return redirect('landing')
'''
        if form.is_valid():
            instance = form.save(commit=False)
            full_name = form.cleaned_data.get('full_name')
            if not full_name:
                full_name = 'New full name'
            instance.full_name = full_name
            instance.save()

            context = {
                'title': 'Thank you!'
            }'''