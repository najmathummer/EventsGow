from django.db import models
from accounts.models import CustomUser
import uuid

# Event model-listView-url-listTemplate
class Tags(models.Model):
    tag_name = models.CharField(max_length=20)
    def __str__(self):
        return self.tag_name
    

class Events(models.Model):
    uuid = uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True) # Primary key attribute
    title = models.CharField(max_length= 50, blank = False) # provides text label for user
    venue = models.CharField(max_length= 30)
    description = models.CharField(max_length= 1024)
    image = models.ImageField(upload_to='images/')
    date = models.DateField()
    time = models.TimeField()
    creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='creator')
    attendees = models.ManyToManyField(CustomUser, related_name='attendees', blank=True)
    favourite = models.ManyToManyField(CustomUser, related_name='favourite', blank=True)
    url = models.CharField(max_length=60)
    tags = models.ManyToManyField(Tags, related_name='tags', blank=True)

    def __str__(self):
        return self.title
