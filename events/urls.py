from django.urls import include, path
from .views import Home

app_name="events"

urlpatterns = [
    path('', Home.as_view(), name='home'), # new
]