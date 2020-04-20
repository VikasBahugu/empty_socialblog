from django.db import models

# Create your models here.
class signup(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=300)
    username = models.CharField(max_length=60)
    number = models.CharField(max_length=60)
    password1 = models.CharField(max_length=300)
    password2 = models.CharField(max_length=300)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.name