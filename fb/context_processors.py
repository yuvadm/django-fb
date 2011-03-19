from django.conf import settings

def fb_app_id(request):
    print 'bla'
    return { settings.FACEBOOK_APP_ID }