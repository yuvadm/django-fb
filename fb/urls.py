from django.conf.urls.defaults import *
from django.http import HttpResponse

urlpatterns = patterns('',
    (r'^$', lambda r: HttpResponse("django-fb base", mimetype="text/plain")),
)