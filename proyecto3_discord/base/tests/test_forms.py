from django.test import TestCase
from base import forms

class FormTests(TestCase):
    def test_user_creation_form(self):
        form = forms.MyUserCreationForm(data={
            'name':'Test user',
            'username': 'test_user',
            'email': 'test_user@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        
        self.assertTrue(form.is_valid())

    def test_user_creation_form_wrong_password(self):
        form = forms.MyUserCreationForm(data={
            'name':'Test user',
            'username': 'test_user',
            'email': 'test_user@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword2'
        })
        
        self.assertFalse(form.is_valid())


    def test_user_creation_form_not_email(self):
        form = forms.MyUserCreationForm(data={
            'name':'Test user',
            'username': 'test_user',
            'email': 'test_user',
            'password1': 'testpassword',
            'password2': 'testpassword'
        })
        
        self.assertFalse(form.is_valid())