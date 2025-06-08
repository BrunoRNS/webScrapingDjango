from django.http import FileResponse, HttpResponseBadRequest
from core.spa_downloader.spa_downloader import SPAStaticDownloader
from django_ratelimit.decorators import ratelimit
from datetime import datetime

from django.conf import settings
from pathlib import Path

BASE_DIR : Path = settings.BASE_DIR

import shutil

@ratelimit(key='ip', rate='3/s', block=True)
def download_zip(request):
        
    print("Starting Download view...") if settings.DEBUG else ...
    
    if request.method != "POST":
        
        print("Bad Request...") if settings.DEBUG else ...
        
        return HttpResponseBadRequest("Only POST requests allowed.")
    
    url = request.POST.get("url")
    
    print(f"Getting url: {url}") if settings.DEBUG else ...
    
    if not url:
        
        return HttpResponseBadRequest("Missing URL.")
    
    print("Generating output_file...") if settings.DEBUG else ...
    
    output_file = BASE_DIR / "tmp" / f"spa_{request.user.id}_{datetime.now()}.zip"
    
    downloader = SPAStaticDownloader(
        url=url,
        output_dir=str(output_file.parent),
        browser="firefox",
        headless=True
    )
    
    print("Starting Downloader...") if settings.DEBUG else ...
    
    downloader.download()
    
    print("Creating zip file...") if settings.DEBUG else ...

    shutil.make_archive(str(output_file).removesuffix(output_file.suffix), 'zip', output_file.parent)

    print("Attaching download as fileresponse...") if settings.DEBUG else ...
    
    response = FileResponse(open(output_file, 'rb'), as_attachment=True, filename="spa_site.zip")
    
    return response
