from django.http import HttpResponse
import datetime
def current_time(request):
    c_time=datetime.datetime.now()
    return HttpResponse(c_time)

