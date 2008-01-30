from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response 
from django_messaging.models import DmMessage
from django_messaging.views import index

def send_pm(request,username):
  if request.user.is_authenticated():
    return render_to_response('messaging/send_pm.html',{'contact_username':username})
  else:
    return HttpResponse('')

def post_pm(request,username):
  profile=request.user.get_profile()
  #pm=DmMessage(user=
  if request.user.is_authenticated():
    return index(request)
  else:
    return HttpResponse('')
