from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import EmailAuthenticationForm
from django.utils.translation import gettext_lazy as _
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    path(_('login/'), auth_views.LoginView.as_view(authentication_form=EmailAuthenticationForm,
                                                template_name='registration/login.html'), name='login'),
    path(_('signup/'), views.SignUpView.as_view(), name='signup'),
    path(_('edit-profile/'), views.UserEditView.as_view(), name='edit'),
]
