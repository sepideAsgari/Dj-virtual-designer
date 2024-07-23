from django.views.generic import TemplateView
from django.urls import path
from . import views

urlpatterns = [
    path('', views.WelcomePageView.as_view(), name='welcome'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('aboutus/', views.AboutUsPageView.as_view(), name='aboutus'),
    path('contactus/', views.ContactUsPageView.as_view(), name='contactus'),
    path('services/', views.ServicesPageView.as_view(), name='services'),
    path('projects/', views.ProjectsPageView.as_view(), name='projects'),
]
