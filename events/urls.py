from django.urls import include, path
from .views import Home, EventCreateView, attend_event, mark_favourite, EventListView, SearchListView, FavouriteEventsListView, CreatedEventsListView, GoingEventsListView, EventUpdateView, EventDetailView

app_name = "events"
urlpatterns = [
    path('', Home.as_view(), name='home'), 
    path('all_events/', EventListView.as_view(), name='all_events'),
    path('search/', SearchListView.as_view(), name='search'), 
    path('favourite/', FavouriteEventsListView.as_view(), name='favourite'),  
    path('created/', CreatedEventsListView.as_view(), name='created'),  
    path('attending/', GoingEventsListView.as_view(), name='attending'),  
    path('create/', EventCreateView.as_view(), name='add_event'),
    path('update_event/<pk>', EventUpdateView.as_view(), name='update_event'),
    path('event/<pk>/', EventDetailView.as_view(), name='event_detail'),
    path('attend_event/', attend_event, name='attend_event'),
    path('mark_favourite/', mark_favourite, name='mark_favourite'),

]
