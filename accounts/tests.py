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


def _create_user(self, username="test123", password="qwer123456"):
    user = get_user_model().objects.create(username=username, is_active=True)
    if password:
        user.set_password(password)
    else:
        user.set_unusable_password()
    user.save()
    return user

class AccountsTests(TestCase):

    def test_Landing_page_status_code(self):
        response = self.client.get('/')
        self.assertEquals(response.status_code, 302)

    def test_view_url_by_name(self):
        response = self.client.get(reverse('events:home'))
        print("===" + str(response) + "\n")
        self.assertEquals(response.url, "/accounts/login/?next=/")

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
        

