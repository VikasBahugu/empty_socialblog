from django.db import models

# Create your models here.
class ContactUS(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=233)
    email = models.CharField(max_length=63)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.email