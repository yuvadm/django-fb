from django.conf import settings

def fb_app_id(request):
    """Add the Facebook app id to template context"""
    return { 'FACEBOOK_APP_ID' : settings.FACEBOOK_APP_ID }