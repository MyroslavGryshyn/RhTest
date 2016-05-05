from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView
from user_management.models import UserProfile


class UserProfileCreate(CreateView):
    model = UserProfile
    fields = '__all__'
    template_name = 'user_form.html'

    # ToDo: change it to home
    def get_success_url(self):
        return reverse('user_add')
