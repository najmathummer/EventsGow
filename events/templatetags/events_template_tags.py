from django import template 
from events.models import Event

register=template.Library()

@register.inclusion_tag('rango/events.html') 
def get_event_list(current_event=None):
    return { 'events': Event.objects.all(),
             'current_event': current_event }
