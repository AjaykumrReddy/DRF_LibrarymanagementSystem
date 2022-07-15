from django.db import models

# Create your models here.


class AdminRegistration(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Library(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    desc = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
