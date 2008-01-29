from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

def send_pm(request,username):
  if request.user.is_authenticated():
    return render_to_response('messaging/send_pm.html',{'to_user':username},context_instance=RequestContext(request))
  else:
    return HttpResponse('')

