from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from locations.models import State, City


class Review(models.Model):
    name = models.CharField(max_length=250)
    logo = models.FileField(upload_to='reviews/')
    city = models.ForeignKey(to=City, on_delete=models.SET_NULL, null=True)
    state = models.ForeignKey(to=State, on_delete=models.SET_NULL, null=True)
    text = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name