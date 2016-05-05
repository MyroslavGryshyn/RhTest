from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from user_management.models import Customer


class CustomerCreateView(CreateView):
    model = Customer
    fields = '__all__'
    template_name = 'user_form.html'

    def get_success_url(self):
        return reverse('home')


class CustomerListView(ListView):
    model = Customer
    template_name = 'user_list.html'
    context_object_name = 'customers'


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = '__all__'
    template_name = 'user_form.html'


    def get_success_url(self):
        return reverse('home')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'user_form.html'


    def get_success_url(self):
        return reverse('home')


