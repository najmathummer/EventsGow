from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from events.forms import EventForm
from django.db.models import Q


from events.models import Events


class Home(LoginRequiredMixin, ListView):
    model = Events
    template_name = "events/home.html"
    context_object_name = 'events'

    def get_queryset(self):
        print("created user", self.request.user)
        queryset = {'all_events': Events.objects.all(), 
                    'favorite_events': Events.objects.filter(favourite=self.request.user),
                    'created_events': Events.objects.filter(creator=self.request.user),
                    'going_events': Events.objects.filter(attendees=self.request.user)
                    
                    }
        return queryset

class EventListView(LoginRequiredMixin, ListView):
    model = Events
    template_name = "events/all_event_list.html"
    context_object_name = 'events'
    queryset = Events.objects.all()



class FavouriteEventsListView(LoginRequiredMixin, ListView):
    model = Events
    template_name = "events/event_list.html"
    context_object_name = 'events'

    def get_queryset(self):
        queryset = Events.objects.filter(favourite=self.request.user)
        return queryset

class CreatedEventsListView(LoginRequiredMixin, ListView):
    model = Events
    template_name = "events/event_list.html"
    context_object_name = 'events'

    def get_queryset(self):
        queryset = Events.objects.filter(creator=self.request.user)
        return queryset

class GoingEventsListView(LoginRequiredMixin, ListView):
    model = Events
    template_name = "events/event_list.html"
    context_object_name = 'events'

    def get_queryset(self):
        queryset = Events.objects.filter(attendees=self.request.user)
        return queryset




class EventCreateView(LoginRequiredMixin,CreateView):
    model = Events
    form_class = EventForm
    success_url = "/"
    def form_valid(self, form):
     
        form.instance.creator = self.request.user
        return super().form_valid(form)

class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Events
    form_class = EventForm
    template_name_suffix = '_update_form'
    success_url = "/"
    def form_valid(self, form):
        return super().form_valid(form)

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Events
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     return context


class SearchListView(LoginRequiredMixin, ListView):
    model = Events
    template_name = "events/all_event_list.html"
    context_object_name = 'events'
    def get_queryset(self):
        print("slef", self.request.GET.get('data'))
        query = self.request.GET.get('data')
        queryset = Events.objects.filter(Q(tags__tag_name__icontains=query) | Q(title__icontains=query))
        return queryset

def attend_event(request):
    if request.method == 'POST':
        event = Events.objects.get(uuid = request.POST.get('event', None) )
        if(request.user not in event.attendees.all()):
            event.attendees.add(request.user)
            return JsonResponse({"status": "Attending"})
        event.attendees.remove(request.user)
        return JsonResponse({"status": "Attend"})

def mark_favourite(request):
    if request.method == 'POST':
        event = Events.objects.get(uuid = request.POST.get('event', None) )
        if(request.user not in event.favourite.all()):
            event.favourite.add(request.user)
            return JsonResponse({"status": "favourite"})
        event.favourite.remove(request.user)
        return JsonResponse({"status": "not favourite"})
         