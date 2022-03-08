from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from events.forms import EventForm


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



class AjaxableResponseMixin:
    """
    Mixin to add AJAX support to a form.
    Must be used with an object-based FormView (e.g. CreateView)
    """
    def form_invalid(self, form):
        print("entered")
        response = super().form_invalid(form)
        if self.request.accepts('text/html'):
            return JsonResponse(form.errors, status=400)
        else:
            return response

    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        print("entered")
        response = super().form_valid(form)
        if self.request.accepts('text/html'):
            data = {
                'pk': self.object.pk,
                'status': 'ok'
            }
            return JsonResponse(data)
        else:
            return response

class EventCreateView(CreateView):
    model = Events
    form_class = EventForm
    # fields = ("title", "venue", "description", "date", "time", "url", "tags")
    success_url = "/"
    def form_valid(self, form):
        # We make sure to call the parent's form_valid() method because
        # it might do some processing (in the case of CreateView, it will
        # call form.save() for example).
        form.instance.creator = self.request.user
        response = super().form_valid(form)
        return super().form_valid(form)
        # if self.request.accepts('text/html'):
        #     data = {
        #         'pk': self.object.pk,
        #         'status': 'ok'
        #     }
        #     return JsonResponse(data)
        # else:
        #     return response

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
         