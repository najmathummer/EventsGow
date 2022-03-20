
from django.views.generic.base import TemplateView

# FAQ Template view
class FAQView(TemplateView):
    
    template_name = "account/faq.html"
