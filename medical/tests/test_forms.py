from django.test import SimpleTestCase
from medical.forms import UserRegisterForm


class testforms(SimpleTestCase):

    def form_data(self):
        form=UserRegisterForm(data={
        'username':'username',
        'email':'email',
        'password1':'password1',
        'password2':'password2'

            })
        self.assertTrue(form.is_valid())

    def form_no_data(self):
        form=UserRegisterForm(data={})

        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors),3)

