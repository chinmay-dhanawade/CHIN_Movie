'''module for all the data to be created'''
import uuid
from django.db import models
from django.contrib.auth.models import User

#MODEL for al movies data
class Movie(models.Model):
    """
    This class has all the essentail compnents which aare used for basic opeerations
    """
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    director = models.CharField(max_length=255)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    average_rating = models.FloatField(default=0.0)
    total_ratings = models.IntegerField(default=0)
    poster = models.FileField(default="leo.jpeg", upload_to="posters")

#model for user to give reeviews and rating
class Review(models.Model):
    """
    This class has all the compnents which are required to 
    add a review and rating to a specific movie
    """
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    