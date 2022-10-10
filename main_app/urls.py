from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_success/', views.contact_sucess_view, name='contact_success'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)