from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static





from . import views



urlpatterns = [
    re_path(r'^$', views.upload,name='landingPage'),
    re_path(r'^success', views.success,name='success'),



]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
