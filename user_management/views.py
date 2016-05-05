from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from user_management.models import UserProfile


class UserProfileCreate(CreateView):
    model = UserProfile
    fields = '__all__'
    template_name = 'user_form.html'

    def get_success_url(self):
        return reverse('home')


class UserProfileList(ListView):
    model = UserProfile
    template_name = 'user_list.html'
