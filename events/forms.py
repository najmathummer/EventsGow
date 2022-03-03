from django import forms 
from events.models import Event

class EventForm(forms.ModelForm):
    # set the field to zero by default. 
    # set the field to be hidden, user won’t be able to enter a value for these fields.
    # we will not include this hidden field at the end because they already be set the default val avoiding the "not null" error
    # for slug, we didnt include it and also set default val because our model will be responsible for populating the field when the form is eventually saved 
    name = forms.CharField(max_length=Event.NAME_MAX_LENGTH,
                           help_text="Please enter the event name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    # An inline class to provide additional information for the form
    class Meta:
        # Provide an association modelform and model
        model = Event
        fields = ('name',)