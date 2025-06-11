### tmp cleaner

from core.utils.tmp_cleaner import run_tmp_cleaner_async

class TmpCleanerMiddleware:
    
    def __init__(self, get_response):
        
        self.get_response = get_response

    def __call__(self, request):
        
        run_tmp_cleaner_async()
        response = self.get_response(request)
        
        return response
