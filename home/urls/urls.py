from home.views import about, home, file_downloader
from django.urls import path

urlpatterns = [
    
    path('', home.home, name='home'),
    path('about/', about.about, name='about'),
    path('download_zip/', file_downloader.download_zip, name='download_zip'),
    
]