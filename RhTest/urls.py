"""RhTest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from customer_management.views import (
    CustomerCreateView, CustomerListView,
    CustomerUpdateView, CustomerDeleteView
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', CustomerListView.as_view(), name='home'),
    url(r'^add/', CustomerCreateView.as_view(), name='customer_add'),
    url(r'^customers/(?P<pk>\d+)/edit/$', CustomerUpdateView.as_view(),
        name='customer_edit'),
    url(r'^customers/(?P<pk>\d+)/delete/$', CustomerDeleteView.as_view(),
        name='customer_delete'),
]
