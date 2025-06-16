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
    """
    Handles the GET request for the home page.

    This function is rate-limited to 5 requests per second from the same IP address.

    Returns a rendered 'home.html' template with the current year in the context.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: The rendered 'home.html' template.
    """
    
    return render(request, "home.html", context)
