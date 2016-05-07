from django.http import HttpResponseRedirect
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

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(CustomerUpdateView, self).post(
                request, *args, **kwargs)

    def get_success_url(self):
        return reverse('home')


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customer_confirm_delete.html'

    def post(self, request, *args, **kwargs):
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(CustomerDeleteView, self).post(
                request, *args, **kwargs)

    def get_success_url(self):
        return reverse('home')


