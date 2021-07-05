from django.test import TestCase,Client
from django.urls import reverse
import json



class testviews(TestCase):


    def testregister(self):
      client=Client()
      response=client.get(reverse('register'))
      self.assertEquals(response.status_code,200)
      self.assertTemplateUsed(response,'register.html')


    def testdoctor_register(self):
      client=Client()
      response=client.get(reverse('doctor_register'))
      self.assertEquals(response.status_code,200)
      self.assertTemplateUsed(response,'doctor_register.html')



    def testlogin(self):
      client=Client()
      response=client.get(reverse('login'))
      self.assertEquals(response.status_code,200)
      self.assertTemplateUsed(response,'login.html')



    def testprofile(self):
      client=Client()
      response=client.get(reverse('profile'))
      self.assertEquals(response.status_code,200)
      self.assertTemplateUsed(response,'error.html')


    def testpatient(self):
      client=Client()
      response=client.get(reverse('patient'))
      self.assertEquals(response.status_code,200)
      self.assertTemplateUsed(response,'error.html')




