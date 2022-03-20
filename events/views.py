from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from events.forms import EventForm
from django.db.models import Q
from events.models import Events


# Home view which render after login
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

# All Event list view
class EventListView(LoginRequiredMixin, ListView):
    model = Events
    template_name = "events/all_event_list.html"
    context_object_name = 'events'
    queryset = Events.objects.all()


# Favourite Event list view
class FavouriteEventsListView(LoginRequiredMixin, ListView):
    model = Events
    template_name = "events/event_list.html"
    context_object_name = 'events'

    def get_queryset(self):
        queryset = Events.objects.filter(favourite=self.request.user)
        return queryset

# Created Event list view
class CreatedEventsListView(LoginRequiredMixin, ListView):
    model = Events
    template_name = "events/event_list.html"
    context_object_name = 'events'

    def get_queryset(self):
        queryset = Events.objects.filter(creator=self.request.user)
        return queryset

# Going Event list view
class GoingEventsListView(LoginRequiredMixin, ListView):
    model = Events
    template_name = "events/event_list.html"
    context_object_name = 'events'

    def get_queryset(self):
        queryset = Events.objects.filter(attendees=self.request.user)
        return queryset



# Event create view
class EventCreateView(LoginRequiredMixin,CreateView):
    model = Events
    form_class = EventForm
    success_url = "/"
    def form_valid(self, form):
     
        form.instance.creator = self.request.user
        return super().form_valid(form)

# Event update view
class EventUpdateView(LoginRequiredMixin, UpdateView):
    model = Events
    form_class = EventForm
    template_name_suffix = '_update_form'
    success_url = "/"
    def form_valid(self, form):
        return super().form_valid(form)

# Event delete view
class EventDeleteView(LoginRequiredMixin, DeleteView):
    model = Events
    success_url = reverse_lazy('events:home')

# Event detail view
class EventDetailView(LoginRequiredMixin, DetailView):
    model = Events


# Event search view
class SearchListView(LoginRequiredMixin, ListView):
    model = Events
    template_name = "events/all_event_list.html"
    context_object_name = 'events'
    def get_queryset(self):
        
        query = self.request.GET.get('data')
        queryset = Events.objects.filter(Q(tags__tag_name__icontains=query) | Q(title__icontains=query)).distinct()
        print("slef", queryset)
        return queryset

# Attend event ajax call
def attend_event(request):
    if request.method == 'POST':
        event = Events.objects.get(uuid = request.POST.get('event', None) )
        if(request.user not in event.attendees.all()):
            event.attendees.add(request.user)
            return JsonResponse({"status": "Attending", "attendees_list": "You and " +str(event.attendees.count()) + " others are going"})
        event.attendees.remove(request.user)
        return JsonResponse({"status": "Attend", "attendees_list": str(event.attendees.count()) + " people are going"})

# Mark Favorite event ajax call
def mark_favourite(request):
    if request.method == 'POST':
        event = Events.objects.get(uuid = request.POST.get('event', None) )
        if(request.user not in event.favourite.all()):
            event.favourite.add(request.user)
            return JsonResponse({"status": "favourite"})
        event.favourite.remove(request.user)
        return JsonResponse({"status": "not favourite"})
         