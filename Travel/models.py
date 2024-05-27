from django.db import models

class UserDetail(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.email