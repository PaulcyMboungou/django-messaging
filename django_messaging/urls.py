from django.conf.urls.defaults import *

urlpatterns = patterns('django_messaging.views',
     (r'^$', 'index'),
     (r'^test/$', 'test'),
     (r'^contacts/$', 'contacts'),
     (r'^contacts/(?P<contact_id>\w+)/add/$', 'add_contact'),
     (r'^contacts/(?P<contact_id>\w+)/remove/$', 'remove_contact'),
     (r'^send_pm/(?P<contact_id>\w+)/$', 'send_pm'),
)
