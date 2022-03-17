
from django.views.generic.base import TemplateView

# Create your views here.
class FAQView(TemplateView):
    
    template_name = "account/faq.html"
