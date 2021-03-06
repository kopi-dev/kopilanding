from django.conf.urls import url

from django.conf import settings
from django.conf.urls.static import static

from .views import LandingView, PrivacyView

urlpatterns = [
    url(r'^$', LandingView.as_view(), name='landing'),
    url(r'^privacy$', PrivacyView.as_view(), name='privacy'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
