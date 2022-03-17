from django.urls import include, path
from .views import FAQView

app_name = "accounts"
urlpatterns = [
    path('', FAQView.as_view(), name='faq'), 

]
