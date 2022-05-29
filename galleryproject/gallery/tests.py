from email.mime import image
from unicodedata import name
from django.test import TestCase
from .models import Image,Location,Category

# Create your tests here.
class CategoryTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.grace= Category(name = 'flowers')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.grace,Category))

class LocationTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.grace= Location(name = 'Nairobi')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.grace,Location))

class ImageTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.grace= Image(image = '/galleryproject/static/images/zebra.jpeg',description ='zebras in the savannah')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.grace,Image))