from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django_messaging.models import DmMessage, DmUser
from django_messaging.controlers import time_to_duration

def test(request):
  msg=''
  if request.user.is_authenticated:
    return render_to_response('messaging/dftest.html',{'message':msg},context_instance=RequestContext(request))
  else:
    return HttpResponse('')

def index(request):
  if request.user.is_authenticated():
    dm_users=DmUser.objects.all().select_related(depth=1).order_by('-last_activity')
    dm_user_current=dm_users.filter(user=request.user)[0]
    dm_user_current_contacts=dm_user_current.contacts.all()
    has_no_contacts=True
    if list(dm_user_current_contacts)<>[]:
      has_no_contacts=False
    #msg=str(dm_user_current.contacts)
    #return render_to_response('debug.html',{'message':msg},context_instance=RequestContext(request))
    user_contacts=[]
    for dm_user in dm_users:
      if dm_user.user<>request.user:
        if dm_user.user in dm_user_current_contacts:
          dm_user.user.activity,is_offline=time_to_duration(dm_user.last_activity)
          dm_user.user.is_online=True
          if is_offline:
            dm_user.user.is_online=False
          dm_user.user.username=dm_user.user.username
          user_contacts.append(dm_user.user) 
    return render_to_response('messaging/index.html',{'has_no_contacts':has_no_contacts,'user_contacts':user_contacts,'media_url':settings.MEDIA_URL},context_instance=RequestContext(request))
  else:
    return HttpResponse('')

