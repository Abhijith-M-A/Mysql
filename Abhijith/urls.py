from django.urls import path

from django.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
	
	path('', include('databaser.urls')),
	
	]

urlpatterns = urlpatterns + static(settings.MEDIA_URL , document_ROOT=settings.MEDIA_ROOT)