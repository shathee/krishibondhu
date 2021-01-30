"""krishiBondhu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from django.conf.urls.i18n import i18n_patterns
from pages import urls as pages_urls
from profiles import urls as profiles_urls
from general import urls as general_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(pages_urls)),
    path('', include(profiles_urls)),
    path('', include(general_urls)),
    url(r'^i18n/', include('django.conf.urls.i18n')), 
    
]


urlpatterns += i18n_patterns(
 # Django Admin
 url(r'^admin/', admin.site.urls),
 url(r'^', include(pages_urls)),
 url(r'^', include(profiles_urls)),
 prefix_default_language=False
)