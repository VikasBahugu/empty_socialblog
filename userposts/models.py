from django.db import models

# Create your models here.
class userpost(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    photo = models.ImageField(upload_to="user_post_photos",blank=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.title