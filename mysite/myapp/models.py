from django.db import models

# Create your models here.


class car(models.Model):
    speed = models.IntegerField()
    color = models.CharField(max_length = 50)
    costs = models.IntegerField()
    img = models.ImageField(upload_to="myapp/static/img", blank=True)



class Animal(models.Model):
    name = models.CharField(max_length = 100)
    sound = models.CharField(max_length = 100)
    


    def speak(self):
        return 10+20 