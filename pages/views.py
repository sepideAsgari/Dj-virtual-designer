from django.utils.decorators import method_decorator
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext as _
from .forms import ContactForm
from django.views import View
from PIL import Image
from .forms import ImageUploadForm
from .models import ImageUpload


@method_decorator(login_required, name='dispatch')
class ServicesPageView(View):
    def get(self, request):
        form = ImageUploadForm()
        images = ImageUpload.objects.filter(user=request.user)
        return render(request, 'pages/services.html', {'form': form, 'images': images})

    def post(self, request):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            images = request.FILES.getlist('image')
            if len(images) > 4:
                return render(request, 'pages/services.html',
                              {'form': form, 'error': _('You cannot upload more than 4 photos.')})

            uploaded_images = []
            for image in images:
                image_instance = ImageUpload(user=request.user, image=image)
                image_instance.save()

                # Open the image file
                img = Image.open(image_instance.image.path)

                # Check orientation and resize accordingly
                if img.width > img.height:
                    img = img.resize((256, 192), Image.LANCZOS)  # Smaller size for display
                else:
                    img = img.resize((192, 256), Image.LANCZOS)  # Smaller size for display

                # Save the resized image
                img.save(image_instance.image.path)
                uploaded_images.append(image_instance.image.url)

            return render(request, 'pages/services.html',
                          {'form': form, 'uploaded_images': uploaded_images, 'upload_success': True})

        return render(request, 'pages/services.html', {'form': form})


class ProjectsPageView(TemplateView):
    template_name = 'pages/projects.html'


class WelcomePageView(TemplateView):
    template_name = 'pages/welcome.html'


class HomePageView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            user = self.request.user  # دریافت اطلاعات کاربر از درخواست
            context.update({
                'username': user.username,
                'email': user.email,
                'first_name': user.first_name,
                'last_name': user.last_name,
            })
        return context


class AboutUsPageView(TemplateView):
    template_name = 'pages/aboutus.html'


class ContactUsPageView(FormView):
    template_name = 'pages/contactus.html'
    form_class = ContactForm
    success_url = reverse_lazy('contactus')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

