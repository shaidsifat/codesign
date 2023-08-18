from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models

class Palette(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    dominant_colors = models.JSONField()
    accent_colors = models.JSONField()
    is_public = models.BooleanField(default=False)

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    palette = models.ForeignKey(Palette, on_delete=models.CASCADE)
