from django.conf.urls.defaults import *

urlpatterns = patterns('django_messaging.views',
     (r'^$', 'index'),
     (r'^test/$', 'test'),
     (r'^contacts/$', 'contacts'),
     #(r'^(?P<title_id>\w+)/$', 'render_blog_post'),
)
