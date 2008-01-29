from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect
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
    #msg=str(dm_user_current.contacts)
    #return render_to_response('debug.html',{'message':msg},context_instance=RequestContext(request))
    user_contacts=[]
    for dm_user in dm_users:
      if dm_user.user<>request.user:
        if dm_user.user in dm_user_current.contacts.all():
          dm_user.user.activity,is_offline=time_to_duration(dm_user.last_activity)
          dm_user.user.is_online=True
          if is_offline:
            dm_user.user.is_online=False
          dm_user.user.username=dm_user.user.username
          user_contacts.append(dm_user.user)
    return render_to_response('messaging/index.html',{'user_contacts':user_contacts},context_instance=RequestContext(request))
  else:
    return HttpResponse('')

def contacts(request):
  if request.user.is_authenticated:
    users=User.objects.all()
    profile=request.user.get_profile()
    contacts=profile.contacts.all()
    messages=''
    num_messages=''
    return render_to_response('messaging/contacts.html',{'users':users,'contacts':contacts,'num_messages':num_messages,'messages':messages},context_instance=RequestContext(request))
  else:
    return HttpResponse('')

def add_contact(request,contact_id):
  if request.user.is_authenticated:
    profile=request.user.get_profile()
    contact=User.objects.get(id=contact_id)
    profile.contacts.add(contact)
    profile.save()
    return contacts(request)
  return HttpResponse('')

def remove_contact(request,contact_id):
  if request.user.is_authenticated:
    profile=request.user.get_profile()
    contact_user=User.objects.get(id=contact_id)
    profile.contacts.remove(contact_user)
    return contacts(request)
  return HttpResponse('')
