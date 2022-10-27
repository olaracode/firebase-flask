def method_allowed(request, method):
    if request != method:
        return True
