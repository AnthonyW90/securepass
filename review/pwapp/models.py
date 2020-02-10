from django.db import models

# Create your models here.


class Password(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=200)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=128)
    lowercase = models.IntegerField()
    uppercase = models.IntegerField()

    def __str__(self):
        return f"{self.name} - {self.username}"
