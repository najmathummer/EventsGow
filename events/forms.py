
from datetime import date, datetime
from django import forms 

from events.models import Events


class EventForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    class Meta:
        model = Events
        fields = ("title","image", "venue", "description", "date", "time", "url", "tags")
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'venue': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={ "class": "form-control"}),
            'url': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput( attrs={'class': 'form-control', 
             'value': date.today,
               'type': 'date'
              }),
            'time': forms.TimeInput(attrs={'class': 'form-control', 
                'value': datetime.now().strftime("%H:%M"),
               'type': 'time'
              }),

        }

