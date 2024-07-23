from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth import get_user_model
from django import forms
from .models import UserProfile
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import PasswordChangeForm as AuthPasswordChangeForm


class EmailAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(label='Email', widget=forms.EmailInput(
        attrs={'autofocus': False, 'class': 'form-control', 'placeholder': 'ایمیل', 'style': 'direction: rtl;'}))

    class Meta:
        model = get_user_model()
        fields = ('username', 'password')


class CustomUserCreationForm(UserCreationForm):
    first_name = forms.CharField(label='نام', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام', 'style': 'direction: rtl;'}))
    last_name = forms.CharField(label='نام خانوادگی', max_length=30, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی', 'style': 'direction: rtl;'}))
    email = forms.EmailField(label='ایمیل', widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'ایمیل', 'style': 'direction: rtl;'}))
    password1 = forms.CharField(label='رمز عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'رمز عبور', 'style': 'direction: rtl;'}))
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور', 'style': 'direction: rtl;'}))

    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("رمز عبور و تکرار آن باید یکسان باشند")

        return cleaned_data


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username',)


# class UserProfileForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['profile_image', 'name', 'email', 'password']
#         widgets = {
#             'password': forms.PasswordInput(render_value=True)  # Render password input as hidden
#         }


class UserEditForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})


class CustomPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور فعلی'}))
    new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور جدید'}))
    new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار رمز عبور جدید'}))

    def clean(self):
        cleaned_data = super().clean()
        new_password1 = cleaned_data.get("new_password1")
        new_password2 = cleaned_data.get("new_password2")

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError("رمزهای عبور جدید با هم مطابقت ندارند.")

        return cleaned_data