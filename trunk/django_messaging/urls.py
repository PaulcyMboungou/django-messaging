from django.conf.urls.defaults import *

urlpatterns = patterns('django_messaging.views',
     (r'^$', 'index'),
     (r'^test/$', 'test'),
     (r'^contacts/$', 'contacts.contacts'),
     (r'^contacts/(?P<contact_id>\w+)/add/$', 'contacts.add_contact'),
     (r'^contacts/(?P<contact_id>\w+)/remove/$', 'contacts.remove_contact'),
     (r'^send_pm/(?P<username>\w+)/$', 'messages.send_pm'),
     (r'^post_pm/(?P<username>\w+)/$', 'messages.post_pm'),
)
