from django.http import FileResponse, HttpResponse
from core.spa_downloader.spa_downloader import SPAStaticDownloader
from django_ratelimit.decorators import ratelimit
from .home import context
from ..forms.forms import UrlForm
from datetime import datetime
from uuid import uuid4
from copy import deepcopy

from django.conf import settings
from pathlib import Path

BASE_DIR : Path = settings.BASE_DIR

import shutil

@ratelimit(key='ip', rate='2/s', block=True)
def download_zip(request):
    """
    Handles the POST request for downloading a static copy of a SPA website.

    This function is rate-limited to 2 requests per second from the same IP address.

    If the request method is not POST, returns a 400 Bad Request response.

    If the input URL is invalid or the reCaptcha is expired, returns a 400 Bad Request response.

    Otherwise, creates a new instance of SPAStaticDownloader with the provided URL and a unique ID,
    downloads the static website, creates a ZIP file out of it, and returns it as a FileResponse with the
    filename "spa_site_<unique_id>.zip".
    """
    
    print("Starting Download view...")
    
    download_zip_context = deepcopy(context)
    
    if request.method != "POST":
        
        download_zip_context["invalid"] = "Invalid request."
        
        return HttpResponse(status=400)
    
    url = UrlForm(request.POST)
    
    if (not url.is_valid()):
        
        download_zip_context["invalid"] = "Invalid input or reCaptcha expired."
        
        return HttpResponse(status=400)

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
        
        if file == output_file or file.is_dir():
            continue
        
        else:
            file.unlink(missing_ok=True)

    print("Attaching download as fileresponse...")
    
    response = FileResponse(open(output_file, 'rb'), as_attachment=True, filename=f"spa_site_{uniqueID}.zip", status=200)
    
    return response
