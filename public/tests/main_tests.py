from django.test import TestCase

# Create your tests here.

#python manage.py test
#https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Testing
from public.models import Product


class PublicTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_false_is_false(self):
        print("Method: test_false_is_false.")
        self.assertFalse(False)

    def test_false_is_true(self):
        print("Method: test_false_is_true.")
        self.assertTrue(False)

    def test_one_plus_one_equals_two(self):
        print("Method: test_one_plus_one_equals_two.")
        self.assertEqual(1 + 1, 2)

    def getProductName(self):
        p = Product.objects.first()
        print(p)


# Run the specified package
# python3 manage.py test public.tests

# Run the specified module
# python3 manage.py test public.tests.main_tests

# Run the specified class
# python3 manage.py test public.tests.main_tests.PublicTest

# Run the specified method
# python3 manage.py test public.tests.main_tests.PublicTest.test_one_plus_one_equals_two