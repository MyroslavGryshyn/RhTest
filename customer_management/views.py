from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.contrib.auth import logout as auth_logout
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from braces.views import LoginRequiredMixin
from customer_management.models import Customer
from customer_management.forms import CustomerCreateForm, CustomerUpdateForm

class LoginPage(TemplateView):
    template_name = 'login.html'


class CustomerCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
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


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('home'))
