from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from events.forms import EventForm 
from django.shortcuts import redirect
from events.models import Event

def index(request):
    context_dict = {}
    response = render( request, 'events/index.html', context=context_dict )
    return response

def event(request):
    context_dict = {}

    event_list = Event.objects.order_by('-likes')[:5] #removed - the results would be in ascending order)
    context_dict['events'] = event_list

    response = render(request, 'events/event.html', context=context_dict)
    return response

def add_event(request):
    form = EventForm();

    if request.method == 'POST':
        form = EventForm(request.POST)

    if form.is_valid():
        evn = form.save(commit=True)
        print(evn, evn.slug)
        return redirect('/events/event')

    else:
        print(form.errors)

    return render(request, 'events/add_event.html', {'form': form})

def show_event(request, event_name_slug):
    context_dict = {}
    try:
        event = Event.objects.get(slug=event_name_slug)
        context_dict['event'] = event
    except Event.DoesNotExist:
        context_dict['event'] = None

    return render(request, 'events/event.html', context = context_dict)