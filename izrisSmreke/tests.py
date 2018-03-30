from django.test import TestCase

from django.test import SimpleTestCase

class Test_izrisa_smreke(SimpleTestCase):

    def test_preveri_stran_vnosa(self):
        odgovor = self.client.get('/')
        self.assertEqual(odgovor.status_code, 200)

    def test_preveri_stran_izrisa(self):
        odgovor = self.client.get('/izris/')
        self.assertEqual(odgovor.status_code, 200)