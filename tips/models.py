from django.db import models

# Create your models here.
class PythonTip(models.Model):
    tip = models.TextField(null=True)
    poster = models.CharField(max_length=50)
    poster_email = models.EmailField(null=True, blank=True)
    timestamp = models.CharField(max_length=20)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.timestamp} - by {self.poster}"