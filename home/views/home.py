from django_ratelimit.decorators import ratelimit
from django.shortcuts import render
from datetime import datetime

@ratelimit(key='ip', rate='5/s', block=True)
def home(request):
    
    context = {
        
        "year": datetime.now().year
    }
    
    return render(request, "home.html", context)
