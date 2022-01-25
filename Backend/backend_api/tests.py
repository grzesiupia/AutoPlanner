# pylint: disable=C0114, W0611
from django.test import SimpleTestCase, TestCase, Client
from django.urls import reverse, resolve
from backend_api.models import Planners
from backend_api.views import add_user
import json

# Create your tests here.


class TestUrls(SimpleTestCase):

    def test_add_user(self):
        url = reverse('user')
        self.assertEquals(resolve(url).func, add_user)


# class TestViews(TestCase):

#     def test_add_user_POST(self):
        
#         email = 'test1@test2@.com'
#         client = Client()
#         url = reverse('user')

#         Planners.objects.create(
#             planneremail = email,
#             login = 'test',
#             password = 'test'
#         )

#         response = client.post(url, {
#             'Sukces': 'Pomyslnie dodano uzytkownika'
#         })

#         self.assertEquals(response.status_code, 200)