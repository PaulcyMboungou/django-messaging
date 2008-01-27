from django.template import RequestContext
from django.shortcuts import render_to_response

def test(request):
  msg=''
  return render_to_response('messaging/dftest.html',{'message':msg},context_instance=RequestContext(request))

def index(request):
  msg=''
  return render_to_response('messaging/index.html',{'message':msg},context_instance=RequestContext(request))

def contacts(request):
  return 
