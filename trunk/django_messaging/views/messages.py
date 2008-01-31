from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response 
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import User
from django_messaging.models import DmMessage
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

def read_first_pm(request):
  if request.user.is_anonymous():
    return HttpResponse('')
  profile=request.user.get_profile()
  messages=DmMessage.objects.filter(user=request.user).order_by('-date')
  message=None
  if list(messages)<>[]:
    #~ get the first unreaded msg
    for msg in messages:
      if msg.readed==False:
        message=msg
        break
  if not message:
    raise ObjectDoesNotExist
  #~ flag the message as readed
  message.readed=True
  message.save()
  return render_to_response('messaging/read_pm.html',{'message':message})

def load_num_msgs(request):
  if request.user.is_anonymous():
    return HttpResponse('')
  profile=request.user.get_profile()
  has_message=False
  if profile.num_messages>0:
    has_message=True
  return render_to_response('messaging/num_messages.html',{'has_message':has_message,'num_messages':profile.num_messages,'media_url':settings.MEDIA_URL})

def load_msgs_list(request):
  if request.user.is_anonymous():
    return HttpResponse('')
  profile=request.user.get_profile()
  has_messages=False
  if profile.num_messages>0:
    has_messages=True
  return render_to_response('messaging/messages_list.html',{'messages':profile.get_messages(),'has_messages':has_messages,'media_url':settings.MEDIA_URL})
