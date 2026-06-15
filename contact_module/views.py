from django.shortcuts import render, redirect
from django.views import View

from site_module.models import SiteSettings
from .forms import ContactUsModelForm
from django.views.generic.edit import FormView, CreateView
from django.views.generic import ListView

from .models import UserProfile


# Create your views here.


class ContactUsView(CreateView):
    template_name = 'contact_module/contact_us_page.html'
    form_class = ContactUsModelForm
    success_url = '/contact-us/'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        settings: SiteSettings = SiteSettings.objects.filter(is_main_settings=True).first()
        context['site_settings'] = settings
        return context


class CreateProfileView(CreateView):
    template_name = 'contact_module/create_profile.html'
    model = UserProfile
    fields = '__all__'
    success_url = '/contact-us/create-profile'


class ProfileView(ListView):
    model = UserProfile
    context_object_name = 'profiles'
    template_name = 'contact_module/ProfileView_list.html'
