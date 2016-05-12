from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import logout as auth_logout
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from braces.views import LoginRequiredMixin
from customer_management.models import Customer, CustomerAdmin
from customer_management.forms import CustomerCreateForm, CustomerUpdateForm


class LoginPage(TemplateView):
    template_name = 'login.html'


class CustomerCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Customer
    template_name = 'customer_form.html'
    form_class = CustomerCreateForm

    def form_valid(self, form):
        # We add owner field from request to disable user to change
        # owner in form
        customer = form.save(commit=False)
        customer.owner = CustomerAdmin.objects.get(user=self.request.user)
        customer.save()
        return super(CustomerCreateView, self).form_valid(form)

    def post(self, request, *args, **kwargs):
        # Overriding post method to grasp Cancel button

        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(CustomerCreateView, self).post(
                request, *args, **kwargs)

    def get_success_url(self):
        return reverse('home')


class CustomerListView(LoginRequiredMixin, ListView):
    login_url = '/login/'
    model = Customer
    template_name = 'customer_list.html'
    context_object_name = 'customers'


class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Customer
    template_name = 'customer_form.html'
    form_class = CustomerUpdateForm

    def post(self, request, *args, **kwargs):
        # Overriding post method to understand if admin has rights to
        # update customer
        object = self.get_object()

        if request.user.id != object.owner.user.id:
            return HttpResponseRedirect(reverse('home'))
        if request.POST.get('cancel_button'):
            return HttpResponseRedirect(reverse('home'))
        else:
            return super(CustomerUpdateView, self).post(
                request, *args, **kwargs)

    def get_success_url(self):
        return reverse('home')


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Customer
    template_name = 'customer_confirm_delete.html'

    def post(self, request, *args, **kwargs):
        # Overriding post method to understand if admin has rights to
        # delete customer
        object = self.get_object()

        if request.user.id != object.owner.user.id:
            return HttpResponseRedirect(reverse('home'))
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


def create_customer_admin(user, **kwargs):
    # Function to create CustomerAdmin record from user
    # during social auth pipeline
    if not CustomerAdmin.objects.filter(user=user):
        CustomerAdmin.objects.create(user=user)
