from django.test import TestCase
from .models import Customer


class CustomerCreateTest(TestCase):

    def test_saving_a_POST_request(self):
        self.client.post(
            '/add/',
            data={'first_name': "John",
                  'last_name': "Doe",
                  'iban': "111111111"}
        )

        self.assertEqual(Customer.objects.count(), 1)
        new_customer = Customer.objects.first()
        self.assertEqual(new_customer.iban, 111111111)

    def test_redirecting_after_POST_request(self):
        response = self.client.post(
            '/add/',
            data={'first_name': "Jane",
                  'last_name': "Doe",
                  'iban': "22222222"}
        )

        self.assertRedirects(response, "/")


class CustomerListTest(TestCase):

    def test_show_no_customers(self):
        response = self.client.get('/')
        self.assertContains(response, "There are no customers yet!")

    def test_show_all_customers(self):
        john_doe = Customer.objects.create(
            first_name="John", last_name="Doe", iban="111111111")
        jane_doe = Customer.objects.create(
            first_name="Jane", last_name="Doe", iban="22222222")

        response = self.client.get('/')

        self.assertContains(response, john_doe.first_name)
        self.assertContains(response, jane_doe.first_name)


class CustomerUpdateTest(TestCase):

    def test_saving_a_POST_request(self):
        Customer.objects.create(
            first_name="John", last_name="Doe", iban="111111111")
        self.client.post(
            '/customers/1/edit/',
            data={'first_name': "Jane",
                  'last_name': "Doe",
                  'iban': "22222222"}
        )

        new_customer = Customer.objects.first()
        self.assertEqual(new_customer.iban, 22222222)

    def test_redirecting_after_POST_request(self):
        Customer.objects.create(
            first_name="John", last_name="Doe", iban="111111111")
        response = self.client.post(
            '/customers/1/edit/',
            data={'first_name': "Jane",
                  'last_name': "Doe",
                  'iban': "22222222"}
        )

        self.assertRedirects(response, "/")


class CustomerDeleteTest(TestCase):

    def test_delete_customer(self):
        Customer.objects.create(
            first_name="John", last_name="Doe", iban="111111111")
        self.client.post('/customers/1/delete/')

        self.assertEqual(Customer.objects.count(), 0)

    def test_deletes_right_customer(self):
        Customer.objects.create(
            first_name="John", last_name="Doe", iban="111111111")
        Customer.objects.create(
            first_name="Jane", last_name="Doe", iban="111111111")

        response = self.client.post('/customers/1/delete/')

        jane_doe = Customer.objects.first()
        self.assertEqual(jane_doe.first_name, "Jane")
