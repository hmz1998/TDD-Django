from django.contrib.auth.forms import UserCreationForm
from django.test import TestCase
from django.urls import reverse

from http import HTTPStatus

from accounts.forms import UserRegistrationForm


class AccountCreationTest(TestCase):
    def setUp(self) -> None:
        self.form_class = UserRegistrationForm

    def test_signup_page_exists(self):
        response = self.client.get(reverse('accounts:signup_page'))

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed('accounts/register.html')
        self.assertContains(response, "Register Form")

    def test_signup_form_works_correctly(self):
        self.assertTrue(issubclass(self.form_class, UserCreationForm))
        self.assertTrue('username' in self.form_class.Meta.fields)
        self.assertTrue('email' in self.form_class.Meta.fields)
        self.assertTrue('password1' in self.form_class.Meta.fields)
        self.assertTrue('password2' in self.form_class.Meta.fields)

        sample_data = {
            "email": "hmz@app.com",
            "username": "hmz",
            "password1": "@Hmz1377528#",
            "password2": "@Hmz1377528#",
        }
        form = self.form_class(sample_data)
        self.assertTrue(form.is_valid())
