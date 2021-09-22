# Middleware Class

import pytz

from django.utils import timezone

class TimezoneMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
        return self.get_response(request)




"""
class MyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # This code is executed before before the 
        # next middleware or view is called
        request.META['CUSTOM_KEY'] = "Nige was here"

        response = self.get_response(request)
        
        # This code is executed after the view is called
        # I.e. on the "return journey"
        assert False
        return response


#Middleware Function

def my_middleware(get_response):
    # Configuration and initialization

    def middleware(request):
        # This code is executed before before the 
        # next middleware or view is called
        request.META['CUSTOM_KEY'] = "Nige was here"

        response = get_response(request)
        
        # This code is executed after the view is called
        # I.e. on the "return journey"
        assert False
        return response

    return middleware

"""