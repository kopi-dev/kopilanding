from django.conf.urls import url

from landing.views import LandingView, LandingRegView

urlpatterns = [
    url(r'^$', LandingView.as_view(), name='landing'),
    #url(r'^reg/', LandingRegView.as_view(), name='landing_success'),
]
