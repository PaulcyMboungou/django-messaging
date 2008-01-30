from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response 
from django.contrib.auth.models import User
#from django_messaging.models import DmMessage
from django_messaging.views import index

def send_pm(request,username):
  if request.user.is_anonymous():
    return HttpResponse('')
  return render_to_response('messaging/send_pm.html',{'contact_username':username})

def post_pm(request,username):
  if request.user.is_anonymous():
    return HttpResponse('')
  profile=request.user.get_profile()
  to_user=User.objects.get(username=username)
  profile.send_message(to_user=to_user,message=request.GET['pm'])
  return index(request)
