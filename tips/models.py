from django.db import models

# Create your models here.
class PythonTip(models.Model):
    tip = models.CharField(max_length=150)
    tweet_link = models.URLField(max_length=200)
    poster = models.CharField(max_length=50)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.tweet_link} - by {self.poster}"