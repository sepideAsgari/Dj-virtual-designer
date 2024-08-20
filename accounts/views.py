from django.contrib.auth import login, update_session_auth_hash
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models.signals import post_save
from django.dispatch import receiver
from .forms import CustomUserCreationForm, UserEditForm, CustomPasswordChangeForm
from .models import CustomUser, UserProfile


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        user = form.save()
        login(self.request, user)
        return response


@method_decorator(login_required, name='dispatch')
class UserEditView(View):
    def get(self, request):
        user_form = UserEditForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)
        return render(request, 'registration/edit_profile.html', {'user_form': user_form, 'password_form': password_form})

    def post(self, request):
        user_form = UserEditForm(instance=request.user)
        password_form = CustomPasswordChangeForm(user=request.user)

        if 'update_profile' in request.POST:
            user_form = UserEditForm(request.POST, instance=request.user)
            if user_form.is_valid():
                user_form.save()
                return redirect('edit')

        elif 'change_password' in request.POST:
            password_form = CustomPasswordChangeForm(data=request.POST, user=request.user)
            if password_form.is_valid():
                user = password_form.save()
                update_session_auth_hash(request, user)
                return redirect('edit')

        return render(request, 'registration/edit_profile.html', {
            'user_form': user_form,
            'password_form': password_form,
        })


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
