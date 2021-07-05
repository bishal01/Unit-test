from django.test import SimpleTestCase
from django.urls import reverse,resolve
from medical.views import *

class testUrls(SimpleTestCase):

    def test_register_urls(self):
        url=reverse('register')
        self.assertEquals(resolve(url).func,register)


    def test_register_urls(self):
        url=reverse('register')
        self.assertEquals(resolve(url).func,register)


    def test_doctor_register_urls(self):
        url=reverse('doctor_register')
        self.assertEquals(resolve(url).func,doctor_register)


    def test_doctor_register_urls(self):
        url=reverse('login')
        self.assertEquals(resolve(url).func,login)


    def test_doctor_register_urls(self):
        url=reverse('profile')
        self.assertEquals(resolve(url).func,profile)


    def test_doctor_register_urls(self):
        url=reverse('patient')
        self.assertEquals(resolve(url).func,patient)


    def test_doctor_register_urls(self):
        url=reverse('doctor')
        self.assertEquals(resolve(url).func,doctor)


    def test_doctor_register_urls(self):
        url=reverse('redirect')
        self.assertEquals(resolve(url).func,profile_redirect)
