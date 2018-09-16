import unittest
from django.urls import reverse
from django.test import Client
from .models import BaseTable
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_basetable(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["CustomerID"] = "CustomerID"
    defaults["Account"] = "Account"
    defaults.update(**kwargs)
    return BaseTable.objects.create(**defaults)


class BaseTableViewTest(unittest.TestCase):
    '''
    Tests for BaseTable
    '''
    def setUp(self):
        self.client = Client()

    def test_list_basetable(self):
        url = reverse('Sample_App_1_basetable_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_basetable(self):
        url = reverse('Sample_App_1_basetable_create')
        data = {
            "name": "name",
            "CustomerID": "CustomerID",
            "Account": "Account",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_basetable(self):
        basetable = create_basetable()
        url = reverse('Sample_App_1_basetable_detail', args=[basetable.pk,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_basetable(self):
        basetable = create_basetable()
        data = {
            "name": "name",
            "CustomerID": "CustomerID",
            "Account": "Account",
        }
        url = reverse('Sample_App_1_basetable_update', args=[basetable.pk,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


