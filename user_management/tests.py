from django.test import TestCase
from .models import UserProfile


class UserProfileCreateTest(TestCase):

    def test_saving_a_POST_request(self):
        self.client.post(
            '/add/',
            data={'first_name': "John",
                  'last_name': "Doe",
                  'iban': "111111111"}
        )

        self.assertEqual(UserProfile.objects.count(), 1)
        new_user_profile = UserProfile.objects.first()
        self.assertEqual(new_user_profile.iban, 111111111)

    def test_redirecting_after_POST_request(self):
        response = self.client.post(
            '/add/',
            data={'first_name': "Jane",
                  'last_name': "Doe",
                  'iban': "22222222"}
        )

        self.assertRedirects(response, "/")


class UserProfileListTest(TestCase):

    def test_show_no_user_profiles(self):
        response = self.client.get('/')
        self.assertContains(response, "There are no user_profiles!")

    def test_show_all_user_profiles(self):
        john_doe = UserProfile.objects.create(
            first_name="John", last_name="Doe", iban="111111111")
        jane_doe = UserProfile.objects.create(
            first_name="Jane", last_name="Doe", iban="22222222")

        response = self.client.get('/')

        self.assertContains(response, john_doe.first_name)
        self.assertContains(response, jane_doe.first_name)
