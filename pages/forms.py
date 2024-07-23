from django import forms
from .models import ImageUpload
from .models import ContactMessage


# class ImageUploadForm(forms.ModelForm):
#     image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
#
#     class Meta:
#         model = ImageUpload
#         fields = ['image']
#

# class ImageUploadForm(forms.ModelForm):
#     class Meta:
#         model = ImageUpload
#         fields = ['image', ]
#         widgets = {
#
#             'image': forms.ClearableFileInput(attrs={'allow_multiple_selected': True})
#
#         }
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True


class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result


class ImageUploadForm(forms.ModelForm):
    image = MultipleFileField(label='بارگذاری عکس', required=False)

    class Meta:
        model = ImageUpload
        fields = ['image', ]


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['first_name', 'last_name', 'email', 'message']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}),
            'email': forms.EmailInput(attrs={'autofocus': False, 'class': 'form-control', 'placeholder': 'ایمیل'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'متن پیام'}),
        }
