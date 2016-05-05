from django.core.urlresolvers import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from customer_management.models import Customer
from customer_management.forms import CustomerCreateForm, CustomerUpdateForm


class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customer_form.html'
    form_class = CustomerCreateForm

    def get_success_url(self):
        return reverse('home')


class CustomerListView(ListView):
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customer_form.html'
    form_class = CustomerUpdateForm


    def get_success_url(self):
        return reverse('home')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_form.html'


    def get_success_url(self):
        return reverse('home')


