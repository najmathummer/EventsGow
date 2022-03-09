from django.urls import include, path
from .views import Home, EventCreateView, attend_event, mark_favourite

app_name="events"
urlpatterns = [
    path('', Home.as_view(), name='home'), # new
     path('create/', EventCreateView.as_view(), name='add_event'),
     path('attend_event/', attend_event, name='attend_event'),
     path('mark_favourite/', mark_favourite, name='mark_favourite'),
   
]