from __future__ import absolute_import
from accounts.models import CustomUser
from django.urls import reverse
from allauth import app_settings as account_settings
from allauth.account.models import EmailAddress
from allauth.account.utils import user_email
from allauth.socialaccount.helpers import complete_social_login
from allauth.socialaccount.models import SocialApp, SocialAccount, SocialLogin
from allauth.utils import get_user_model
from django.contrib.auth.models import AnonymousUser
from django.contrib.auth.models import User
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.test import TestCase

from django.test.client import RequestFactory
from django.test.utils import override_settings
from django.contrib.auth import get_user_model 
from django.conf import settings
from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.contrib.messages.api import get_messages
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.test.client import Client, RequestFactory
from django.test.utils import override_settings
from django.urls import reverse
from django.utils.timezone import now
from allauth.account.models import (
    EmailAddress,
    EmailConfirmation,
    EmailConfirmationHMAC,
)
from allauth.tests import Mock, TestCase, patch
from allauth.utils import get_user_model, get_username_max_length
from allauth.account.signals import user_logged_in, user_logged_out
from allauth.account.utils import (
    filter_users_by_username,
    url_str_to_user_pk,
    user_pk_to_url_str,
    user_username,
)
from allauth.account.auth_backends import AuthenticationBackend

class EventsTest(TestCase):
    
    username = 'test@student.gla.ac.uk'
    password = 'testtesttest'

    def test_create_user_login(self):
        

        new_user = CustomUser.objects.create_user(
            username = self.username,
            email = self.username,
            password = self.password,
            )
        new_user.save()
        new_user.is_active = True
        new_user.save()

        new_email_address = EmailAddress(
            user_id=new_user.id,
            email=self.username,
            verified=True,
            primary=True,
            )
        new_email_address.save()

        # test loggin 
    def test_login(self):
        self.test_create_user_login()
        logged_in = self.client.login(email = self.username, password = self.password)
        self.assertTrue(logged_in)  # return true

    def test_redirect_url(self):  # test redirect url
        self.test_create_user_login()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

        # test home page contains correct html
    def test_redirect_url(self):  # test redirect url
        self.test_create_user_login()
        self.username = "test"
        self.test_login()
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/home.html')
        self.assertTemplateUsed(response, 'events/base.html')

        # test view url by name
    def test_view_url_by_name(self):
        self.test_create_user_login()
        self.username = "test1"
        self.test_login()
        response = self.client.get('/created/')
        self.assertEquals(response.status_code, 200)

        # test view url by name
    def test_view_url_by_name(self):
        self.test_create_user_login()
        self.username = "test2"
        self.test_login()
        response = self.client.get('/favourite/')
        self.assertEquals(response.status_code, 200)

        # test view url by name
    def test_view_url_by_name(self):
        self.test_create_user_login()
        self.username = "test3"
        self.test_login()
        response = self.client.get('/attending/')
        self.assertEquals(response.status_code, 200)

    def test_password_reset_get(self):
        resp = self.client.get(reverse("account_reset_password"))
        self.assertTemplateUsed(resp, "account/password_reset.html")

 
