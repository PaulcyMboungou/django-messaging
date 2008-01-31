from django.http import HttpResponse, HttpResponseRedirect
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

def read_pm(request,message_id=None,first=False):
  if request.user.is_anonymous():
    return HttpResponse('')
  profile=request.user.get_profile()
  if first:
    messages=profile.get_messages()
    message=None
    if list(messages)<>[]:
      #~ get the first unreaded msg
      for msg in messages:
        if msg.readed==False:
          message=msg
          break
  else:
    try:
      message=DmMessage.objects.get(id=message_id,user=request.user)
    except ObjectDoesNotExist:
      #~ this guy is trying to read other user's pm
      return HttpResponse('Non je crois pas ...')
  if not message:
    return HttpResponse('Impossible de lire le message')
  #~ update num_messages
  if message.readed==False:
    profile.num_messages=profile.num_messages-1
  #~ flag the message as readed
  message.readed=True
  #~ save data
  profile.save()
  message.save()
  return render_to_response('messaging/read_pm.html',{'message':message})

def read_first_pm(request):
  return read_pm(request,first=True)

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
  messages=profile.get_messages().order_by('-date')
  if len(list(messages))>0:
    has_messages=True
  return render_to_response('messaging/messages_list.html',{'messages':messages,'has_messages':has_messages,'media_url':settings.MEDIA_URL})

def delete_message(request,message_id):
  if request.user.is_anonymous():
    return HttpResponse('')
  profile=request.user.get_profile() 
  profile.delete_message(int(message_id)) 
  return HttpResponse('')
