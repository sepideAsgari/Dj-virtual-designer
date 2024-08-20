from django.views.generic import TemplateView
from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

urlpatterns = [
    path('', views.WelcomePageView.as_view(), name='welcome'),
    path(_('home/'), views.HomePageView.as_view(), name='home'),
    path(_('aboutus/'), views.AboutUsPageView.as_view(), name='aboutus'),
    path(_('contactus/'), views.ContactUsPageView.as_view(), name='contactus'),
    path(_('services/'), views.ServicesPageView.as_view(), name='services'),
    path(_('projects/'), views.ProjectsPageView.as_view(), name='projects'),
]
