from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from user_management.models import Customer


class CustomerCreate(CreateView):
    model = Customer
    fields = '__all__'
    template_name = 'user_form.html'

    def get_success_url(self):
        return reverse('home')


class CustomerList(ListView):
    model = Customer
    template_name = 'user_list.html'
    context_object_name = 'customers'


class CustomerUpdate(UpdateView):
    model = Customer
    fields = '__all__'
    template_name = 'user_form.html'

    def get_success_url(self):
        return reverse('home')
