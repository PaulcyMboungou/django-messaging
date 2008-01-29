from django.template import RequestContext
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.auth.models import User

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
