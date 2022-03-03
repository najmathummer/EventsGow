from django.urls import path
from events import views

app_name = 'events'
urlpatterns = [

    path('', views.index, name='index'),
    path('event/', views.event, name='event'),
    path('add_event/', views.add_event, name='add_event'),
    path('event/<slug:event_name_slug>/',
        views.show_event, name='show_event'),
]