from django.conf.urls.defaults import *
from django.contrib import admin
from django.http import HttpResponse

admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', lambda r: HttpResponse("demo base", mimetype="text/plain")),
    
    (r'^fb/', include('fb.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
