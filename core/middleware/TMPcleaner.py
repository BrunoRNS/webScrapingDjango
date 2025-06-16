### tmp cleaner

from core.utils.tmp_cleaner import run_tmp_cleaner_async

class TmpCleanerMiddleware:
    
    def __init__(self, get_response):
        """
        Initializes the middleware with a get_response method.

        :param get_response: A method that takes a request and returns a response.
        :type get_response: callable
        """
        
        self.get_response = get_response

    def __call__(self, request):
        """
        Calls the get_response method and runs the tmp cleaner in a background thread.

        The tmp cleaner is run as a background thread to prevent blocking the main thread.
        The get_response method is called with the request and the response is returned.

        :param request: The request object.
        :type request: HttpRequest
        :return: The response.
        :rtype: HttpResponse
        """
        
        run_tmp_cleaner_async()
        response = self.get_response(request)
        
        return response
