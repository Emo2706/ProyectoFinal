from django.db import models

# Create your models here.

class User(models.Model):

    name = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return f'Name: {self.name} - City: {self.city} - Age: {self.age} - E-Mail {self.email}'

class Games(models.Model):

    name = models.CharField(max_length=30)
    developer = models.CharField(max_length=30)
    popularity = models.IntegerField()
    type = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Games"
        verbose_name_plural = "Games"

    def __str__(self):
        return f'Name: {self.name} - Developer: {self.developer} - Popularity: {self.popularity} - Type {self.type}'

class Creators(models.Model):

    username = models.CharField(max_length=30)
    platforms = models.CharField(max_length=30)
    subscriptions = models.IntegerField()

    class Meta:
        verbose_name = "Creators"
        verbose_name_plural = "Creators"

    def __str__(self):
        return f'Username: {self.username} - Platforms: {self.platforms} - Subscriptions: {self.subscriptions}'    
