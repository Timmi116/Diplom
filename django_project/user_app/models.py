from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=100, null=True)
    password = models.CharField(max_length=100, null=True)
    age = models.IntegerField(null=True)
    gender = models.CharField(max_length=10, null=True)
    email = models.EmailField(unique=True)
    date_of_birth = models.DateField(null=True)
    place_of_birth = models.CharField(max_length=100, null=True)
    address = models.TextField(null=True)
    biography = models.TextField(null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True)

    def __str__(self):
        return self.username