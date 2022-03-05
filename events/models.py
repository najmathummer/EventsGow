from django.db import models

# Event model-listView-url-listTemplate
class Tags(models.Model):
    id = models.IntegerField(primary_key=True)
    tag_name = models.CharField(max_length=20)
    

class Events(models.Model):

    uuid = models.UUIDField(default=uuid.uuid4, editable=false, primary_key=True) # Primary key attribute
    title = models.CharField(max_length= 128, help_text='Enter the title of the event here', blank = False) # provides text label for user
    venue = models.CharField(max_length= 512, help_text='Enter the venue of the event here')
    description = models.CharField(max_length= 1024, help_text='Enter the description of the event here')
    date = models.DateField(max_length= 10)
    time = models.TimeField(max_length= 5)
    image = models.FileField(upload_to='images/')
    favourite = models.IntegerField()
    url = models.CharField(max_length=60)
    creator = models.ForeignKey(
        'Creator',
        on_delete=models.CASCADE,
    )
    attendees = models.ManyToManyField()
    
    
class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=150)
    password = models.CharField(max_length=128)
    email = models.CharField(max_length=75)
    is_superuser = models.BooleanField()