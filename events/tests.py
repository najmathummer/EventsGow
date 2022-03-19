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
from django.test.client import Client
from django.test.client import RequestFactory
from django.test.utils import override_settings

from django.contrib.auth import get_user_model 



import json
import uuid
from datetime import timedelta

from django import forms
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.models import AbstractUser, AnonymousUser
from django.contrib.messages.api import get_messages
from django.contrib.messages.middleware import MessageMiddleware
from django.contrib.sessions.middleware import SessionMiddleware
from django.core import mail, validators
from django.core.exceptions import ValidationError
from django.db import models
from django.http import HttpResponseRedirect
from django.template import Context, Template
from django.test.client import Client, RequestFactory
from django.test.utils import override_settings
from django.urls import reverse
from django.utils.timezone import now
import allauth.app_settings
from allauth.account.forms import BaseSignupForm, ResetPasswordForm, SignupForm
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

class LoginTest(TestCase):
    # def _create_user(self, username="test", password="qwer123", **kwargs):
    #     user = get_user_model().objects.create(
    #         username=username, is_active=True, **kwargs
    #     )
    #     if password:
    #         user.set_password(password)
    #     else:
    #         user.set_unusable_password()
    #     user.save()
    #     return user

    # def _create_user_and_login(self, usable_password=True):
    #     password = "doe" if usable_password else False
    #     user = self._create_user(password=password)
    #     self.client.force_login(user)
    #     return user

    # def test_redirect_when_authenticated(self):
    #     self._create_user_and_login()
    #     c = self.client
    #     resp = c.get(reverse("account_login"))
    #     self.assertRedirects(resp, "/", fetch_redirect_response=False)

    def test_create_user_login(self):
        username = 'test@student.gla.ac.uk'
        password = 'testtesttest'

        new_user = CustomUser.objects.create_user(
            username=username,
            email=username,
            password=password,
            )
        new_user.save()
        new_user.is_active = True
        new_user.save()

        new_email_address = EmailAddress(
            user_id=new_user.id,
            email=username,
            verified=True,
            primary=True,
            )
        new_email_address.save()

        # test loggin 
        logged_in = self.client.login(email=username, password=password)
        self.assertTrue(logged_in)  # return true

        # test redirect url
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)

        # test home page contains correct html
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'events/home.html')
        self.assertTemplateUsed(response, 'events/base.html')

        # test view url by name
        response = self.client.get('/created/')
        self.assertEquals(response.status_code, 200)

        # test view url by name
        response = self.client.get('/favourite/')
        self.assertEquals(response.status_code, 200)

        # test view url by name
        response = self.client.get('/attending/')
        self.assertEquals(response.status_code, 200)

        



    @patch('django.contrib.auth.middleware.get_user', return_value=CustomUser.objects.first())
    def test_home_page_status_code(self, patch):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)

    

    def test_password_reset_get(self):
        resp = self.client.get(reverse("account_reset_password"))
        self.assertTemplateUsed(resp, "account/password_reset.html")

    

    
#     @override_settings(
#         ACCOUNT_EMAIL_CONFIRMATION_HMAC=True,
#         ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION=True,
#     )
#     def test_login_on_confirm(self):
#         user = _create_user(self)
#         email = EmailAddress.objects.create(
#             user=user, email="test@student.gla.ac.uk", verified=False, primary=True
#         )
#         key = EmailConfirmationHMAC(email).key

        # receiver_mock = Mock()  # we've logged if signal was called
        # user_logged_in.connect(receiver_mock)

        # fake post-signup account_user stash
        # session = self.client.session
        # session["account_user"] = user_pk_to_url_str(user)
        # session.save()

        # resp = self.client.post(reverse("account_confirm_email", args=[key]))
        # email = EmailAddress.objects.get(pk=email.pk)
        # self.assertTrue(email.verified)

        # receiver_mock.assert_called_once_with(
        #     sender=get_user_model(),
        #     request=resp.wsgi_request,
        #     response=resp,
        #     user=get_user_model().objects.get(username="test123"),
        #     signal=user_logged_in,
        # )

        # user_logged_in.disconnect(receiver_mock)

def _create_user(self, username="test123", password="qwer123456"):
    user = get_user_model().objects.create(username=username, is_active=True)
    if password:
        user.set_password(password)
    else:
        user.set_unusable_password()
    user.save()
    return user

class HomePageTests(TestCase):
    @override_settings(
        ACCOUNT_EMAIL_CONFIRMATION_HMAC=True,
        ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION=True,
    )
    def test_Email_verified(self):
        user = _create_user(self)
        email = EmailAddress.objects.create(
            user=user, email="test@student.gla.ac.uk", verified=False, primary=True
        )
        key = EmailConfirmationHMAC(email).key
        receiver_mock = Mock()
        user_logged_in.connect(receiver_mock)
        session = self.client.session
        session["account_user"] = user_pk_to_url_str(user)
        session.save()
        resp = self.client.post(reverse("account_confirm_email", args=[key]))
        email = EmailAddress.objects.get(pk=email.pk)
        self.assertTrue(email.verified)
        receiver_mock.assert_called_once_with(
            sender=get_user_model(),
            request=resp.wsgi_request,
            response=resp,
            user=get_user_model().objects.get(username="test123"),
            signal=user_logged_in,
        )

        user_logged_in.disconnect(receiver_mock)
        
        


    # def test_view_url_by_name(self):
    #     response = self.client.get(reverse('/Home'))
    #     self.assertEquals(response.status_code, 302)

    # def test_view_uses_correct_template(self):
    #     response = self.client.get(reverse('home'))
    #     self.assertEquals(response.status_code, 302)
    #     self.assertTemplateUsed(response, 'home.html')




# # class HomePageTests(TestCase):

#     # def test_home_page_status_code(self):
#     #     response = self.client.get('/')
#     #     self.assertEquals(response.status_code, 302)

#     # def test_view_url_by_name(self):
#     #     response = self.client.get(reverse('home'))
#     #     self.assertEquals(response.status_code, 302)

#     # def test_view_uses_correct_template(self):
#     #     response = self.client.get(reverse('home'))
#     #     self.assertEquals(response.status_code, 302)
#         # self.assertTemplateUsed(response, 'home.html')

#     # def test_home_page_contains_correct_html(self):
#     #     response = self.client.get('/')
#     #     self.assertContains(response, '<h1>Homepage</h1>')

#     # def test_home_page_does_not_contain_incorrect_html(self):
#     #     response = self.client.get('/')
#     #     self.assertNotContains(
#     #         response, 'Hi there! I should not be on the page.')

class AuthenticationBackendTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create(
            is_active=True, email="test@student.gla.ac.uk", username="test"
        )
        user.set_password(user.username)
        user.save()
        self.user = user

    @override_settings (
        ACCOUNT_AUTHENTICATION_METHOD= 'USERNAME',
    )
    def test_auth_by_username(self):
        user = self.user
        backend = AuthenticationBackend()
        self.assertEqual(
            backend.authenticate(
                request=None, username=user.username, password=user.username
            ).pk,
            user.pk,
        )
        self.assertEqual(
            backend.authenticate(
                request=None, username=user.email, password=user.username
            ),
            None,
        )