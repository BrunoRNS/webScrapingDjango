from django_ratelimit.decorators import ratelimit
from django.shortcuts import render
from ..forms.forms import UrlForm
from datetime import datetime

context = {
        
    "year": datetime.now().year,
    "form": UrlForm,
    "invalid": "",
        
}

@ratelimit(key='ip', rate='5/s', block=True)
def home(request):
    
    return render(request, "home.html", context)
