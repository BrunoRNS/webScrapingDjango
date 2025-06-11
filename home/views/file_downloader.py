from django.http import FileResponse, HttpResponseBadRequest
from core.spa_downloader.spa_downloader import SPAStaticDownloader
from django_ratelimit.decorators import ratelimit
from ..forms.forms import UrlForm
from datetime import datetime
from uuid import uuid4

from django.conf import settings
from pathlib import Path

BASE_DIR : Path = settings.BASE_DIR

import shutil

@ratelimit(key='ip', rate='2/s', block=True)
def download_zip(request):
    
    print("Starting Download view...")
    
    if request.method != "POST":
        
        print("Bad Request...")
        
        return HttpResponseBadRequest("Only POST requests allowed.")
    
    url = UrlForm(request.POST)
    
    if not url.is_valid():
        
        print("Bad Request...")
        
        return HttpResponseBadRequest("Invalid request form, aborting...")
    
    uniqueID: str = uuid4().hex
    
    output_file = BASE_DIR / "tmp" / f"{uniqueID}" / f"spa_{datetime.now()}.zip"
    
    downloader = SPAStaticDownloader(
        url=url.cleaned_data['input_url'],
        output_dir=str(output_file.parent),
        browser="firefox",
        headless=True
    )
    
    print("Starting Downloader...")
    
    downloader.download()
    
    print("Creating zip file...")

    shutil.make_archive(str(output_file).removesuffix(output_file.suffix), 'zip', output_file.parent)

    # Remove all files except the zip one before send to the client
    
    for file in output_file.parent.rglob("*"):
        
        if file == output_file:
            continue
        
        else:
            file.unlink(missing_ok=True)

    print("Attaching download as fileresponse...")
    
    response = FileResponse(open(output_file, 'rb'), as_attachment=True, filename=f"spa_site_{uniqueID}.zip")
    
    return response
