from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

from accounts.models import CustomUser


# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=69)
    purchaser = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    desc = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('game_list')
