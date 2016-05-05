from django.views.generic.edit import CreateView
from user_management.models import UserProfile


class UserProfileCreate(CreateView):
    model = UserProfile
    fields = '__all__'
    template_name = 'user_form.html'
    success_url = 'home'
