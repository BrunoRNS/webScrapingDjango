from django.http import FileResponse, HttpResponseBadRequest
from core.spa_downloader.spa_downloader import SPAStaticDownloader
from ratelimit.decorators import ratelimit
from datetime import datetime

from WebScrapingDjango.settings import BASE_DIR 

import shutil

@ratelimit(key='ip', rate='7/s', block=True)
def download_spa_zip(request):
    
    if request.method != "POST":
        
        return HttpResponseBadRequest("Only POST requests allowed.")
    
    url = request.POST.get("url")
    
    if not url:
        
        return HttpResponseBadRequest("Missing URL.")
    
    output_file = BASE_DIR / "tmp" / f"spa_{request.user.id}_{datetime.now()}.zip"
    
    downloader = SPAStaticDownloader(
        url=url,
        output_dir=str(output_file.parent),
        browser="firefox",
        headless=True
    )
    
    downloader.download()

    shutil.make_archive(str(output_file).removesuffix(output_file.suffix), 'zip', output_file.parent)

    response = FileResponse(open(output_file, 'rb'), as_attachment=True, filename="spa_site.zip")
    
    return response
