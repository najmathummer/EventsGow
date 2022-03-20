from django.urls import include, path
from .views import Home, EventCreateView, attend_event, mark_favourite, EventListView, SearchListView, FavouriteEventsListView, CreatedEventsListView, GoingEventsListView, EventUpdateView, EventAttendeesDetailView, EventDetailView, EventDeleteView

app_name = "events"
urlpatterns = [
    path('', Home.as_view(), name='home'), 
    path('all_events/', EventListView.as_view(), name='all_events'),
    path('created/', CreatedEventsListView.as_view(), name='created'),  
    path('favourite/', FavouriteEventsListView.as_view(), name='favourite'),  
    path('attending/', GoingEventsListView.as_view(), name='attending'),  
    path('attendees/<pk>/', EventAttendeesDetailView.as_view(), name='event_attendees'),
    path('event/<pk>/', EventDetailView.as_view(), name='event_detail'),
    path('create/', EventCreateView.as_view(), name='add_event'),
    path('update_event/<pk>', EventUpdateView.as_view(), name='update_event'),
    path('delete_event/<pk>', EventDeleteView.as_view(), name='delete_event'),
    path('search/', SearchListView.as_view(), name='search'), 
    path('attend_event/', attend_event, name='attend_event'),
    path('mark_favourite/', mark_favourite, name='mark_favourite'),

]
