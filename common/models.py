from django.db import models
from django.contrib.auth.models import User

class CharacterDB(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    text = models.CharField(max_length=100)