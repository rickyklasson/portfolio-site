from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact_success/', views.contact_sucess_view, name='contact_success'),
]