from django_ratelimit.decorators import ratelimit
from django.shortcuts import render
from datetime import datetime

@ratelimit(key='ip', rate='5/s', block=True)
def about(request):
    """
    Renders the 'about' page with the current year in the context.

    This view is rate-limited to 5 requests per second from the same IP address.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpResponse: The rendered 'about.html' template.
    """

    context = {
        
        "year": datetime.now().year
    }
    
    return render(request, "about.html", context)
