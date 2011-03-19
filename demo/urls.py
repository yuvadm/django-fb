from django.conf.urls.defaults import *
from django.contrib import admin
from django.http import HttpResponse
from django.template import Context, loader


admin.autodiscover()

urlpatterns = patterns('',
    (r'^$', 'demo.main.views.index'),
    
    (r'^fb/', include('fb.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
