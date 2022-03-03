from django.db import models
from django.template.defaultfilters import slugify


class Event( models.Model ):

    NAME_MAX_LENGTH = 128 
    name = models.CharField( max_length=NAME_MAX_LENGTH, unique=True )
    likes = models.IntegerField( default=0 )
    slug = models.SlugField( unique=True )
    
    # @ override
    def save(self, *args, **kwargs):
        self.slug = slugify( self.name ) 
        super( Event, self ).save( *args, **kwargs )

    class Meta:
        verbose_name_plural = 'Events'

    def __str__(self): 
        return self.name