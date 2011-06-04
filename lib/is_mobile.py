def is_mobile(request):
    '''
    This function checks the user agent string for tell-tale signs of a mobile browser. I'm not picky really, iPads are
    fine too, as is any Android device.

    Based on the minidetector middleware: http://code.google.com/p/minidetector/
    '''
    if request.META.has_key("HTTP_USER_AGENT"):
        s = request.META["HTTP_USER_AGENT"].lower()

        #if 'applewebkit' in s:
        #    return True

        if 'ipad' in s:
            return True

        if 'iphone' in s or 'ipod' in s:
            return True

        if 'android' in s:
            return True

        if 'webos' in s:
            return True

        if 'windows phone' in s:
            return True

    return False
