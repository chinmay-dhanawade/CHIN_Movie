from django.db import models
import uuid


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    director = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #rating = models.DecimalField(max_digits=5, decimal_places=1, default=0)
    