from django.test import TestCase

# Create your tests here.




from myapp.models import Animal
class Animaltestcase(TestCase):
    def setup(self):
        Animal.objects.create(name="lion", sound="roar")
        Animal.objects.create(name="cat", sound="meow")
    def test_amimals_can_speak(self):
        """Animals than can speak are correcrly identified"""
        lion = Animal.objects.get(name="lion")
        cat = Animal.objects.get(name="cat")
        self.assertEqual(lion.speak(), 30)
        self.assertEqual(cat.speak(), 30)
#1