from django.test import TestCase
from .models import Customer

from django.contrib.auth.models import User
from django.test import Client

from django.core.urlresolvers import reverse


class CustomerCreateTest(TestCase):

    def setUp(self):
        self.client = Client()
        john = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.force_login(john)

    def test_login_works(self):
        response = self.client.get(reverse('customer_add'))
        self.assertEqual(response.status_code, 200)

    def test_saving_a_POST_request(self):
        self.client.post(
            '/add/',
            data={'first_name': "John",
                  'last_name': "Doe",
                  'iban': "DE89370400440532013000"}
        )

        self.assertEqual(Customer.objects.count(), 1)
        new_customer = Customer.objects.first()
        self.assertEqual(new_customer.iban,  "DE89370400440532013000")

    def test_redirecting_after_POST_request(self):
        response = self.client.post(
            '/add/',
            data={'first_name': "Jane",
                  'last_name': "Doe",
                  'iban': "DE89370400440532013000"}
        )

        self.assertRedirects(response, "/")

    def test_invalid_iban(self):
        self.client.post(
            '/add/',
            data={'first_name': "John",
                  'last_name': "Doe",
                  'iban': "GB82WEST1234569876543"}
        )

        self.assertEqual(Customer.objects.count(), 0)

    def test_duplicate_iban(self):
        self.client.post(
            '/add/',
            data={'first_name': "John",
                  'last_name': "Doe",
                  'iban': "DE89370400440532013000"}
        )

        self.assertEqual(Customer.objects.count(), 1)

        self.client.post(
            '/add/',
            data={'first_name': "Jane",
                  'last_name': "Doe",
                  'iban': "DE89370400440532013000"}
        )

        self.assertEqual(Customer.objects.count(), 1)

    def test_authentification_required(self):
        self.client.logout()

        self.client.post(
            '/add/',
            data={'first_name': "Jane",
                  'last_name': "Doe",
                  'iban': "DE89370400440532013000"}
        )

        self.assertEqual(Customer.objects.count(), 0)


class CustomerListTest(TestCase):

    def test_show_no_customers(self):
        response = self.client.get('/')
        self.assertContains(response, "There are no customers yet!")

    def test_show_all_customers(self):
        john_doe = Customer.objects.create(
            first_name="John", last_name="Doe", iban="DE89370400440532013000")
        jane_doe = Customer.objects.create(
            first_name="Jane", last_name="Doe", iban="DE89370400440532013001")

        response = self.client.get('/')

        self.assertContains(response, john_doe.first_name)
        self.assertContains(response, jane_doe.first_name)


class CustomerUpdateTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            'john', 'lennon@thebeatles.com', 'johnpassword')
        self.client.login(username='john', password='johnpassword')

    def test_saving_a_POST_request(self):
        Customer.objects.create(
            first_name="John", last_name="Doe", iban="DE89370400440532013000")
        self.client.post(
            '/customers/1/edit/',
            data={'first_name': "Jane",
                  'last_name': "Doe",
                  'iban': "AL47 2121 1009 0000 0002 3569 8741"}
        )

        new_customer = Customer.objects.first()
        self.assertEqual(new_customer.iban, "AL47212110090000000235698741")

    def test_redirecting_after_POST_request(self):
        Customer.objects.create(
            first_name="John", last_name="Doe", iban="DE89370400440532013000")
        response = self.client.post(
            '/customers/1/edit/',
            data={'first_name': "Jane",
                  'last_name': "Doe",
                  'iban': "AL47 2121 1009 0000 0002 3569 8741"}
        )

        self.assertRedirects(response, "/")

    def test_login_required_for_update(self):
        self.client.logout()
        self.client.login(username='jo', password='johnpassword')

        self.client.post(
            '/add/',
            data={'first_name': "Jane",
                  'last_name': "Doe",
                  'iban': "DE89370400440532013000"}
        )

        self.assertEqual(Customer.objects.count(), 0)


class CustomerDeleteTest(TestCase):

    def test_delete_customer(self):
        Customer.objects.create(
            first_name="John", last_name="Doe", iban="DE89370400440532013001")
        self.client.post('/customers/1/delete/')

        self.assertEqual(Customer.objects.count(), 0)

    def test_deletes_right_customer(self):
        Customer.objects.create(
            first_name="John", last_name="Doe", iban="DE89370400440532013000")
        Customer.objects.create(
            first_name="Jane", last_name="Doe", iban="DE89370400440532013001")

        self.client.post('/customers/1/delete/')

        jane_doe = Customer.objects.first()
        self.assertEqual(jane_doe.first_name, "Jane")

    def test_redirecting_after_deletion(self):
        Customer.objects.create(
            first_name="John", last_name="Doe", iban="DE89370400440532013000")

        response = self.client.post('/customers/1/delete/')

        self.assertRedirects(response, "/")
