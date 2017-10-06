"""softwareII URL Configuration"""

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    # Admin urls
    url(r'^admin/', admin.site.urls),
    # Main Views
    url(r'^', include('main.urls')),
    # Auth urls 
    url(r'^user/', include('django.contrib.auth.urls')),
    # User Views
    url(r'^user/', include('users.urls', namespace='users')),
]
