from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import EmailAuthenticationForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(authentication_form=EmailAuthenticationForm,
                                                template_name='registration/login.html'), name='login'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('edit-profile/', views.UserEditView.as_view(), name='edit'),
]
