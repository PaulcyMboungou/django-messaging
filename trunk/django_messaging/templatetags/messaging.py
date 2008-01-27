from django import template
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.models import SiteProfileNotAvailable

register = template.Library()

@register.tag
def messaging(parser,token):
  nodelist=parser.parse(('endmessaging',))
  parser.delete_first_token()
  return MessagingNode(nodelist)

class MessagingNode(template.Node):
  def __init__(self,nodelist):
    self.nodelist=nodelist

  def render(self,context):
    user=context['user']
    try:
      dm_user=user.get_profile()
    except SiteProfileNotAvailable:
      return 'no conf'
    except ObjectDoesNotExist:
      return 'no user'
    except Exception, e:
      return str(e)
    context['has_message']=False
    if dm_user.num_messages>0:
      context['has_message']=True
    context['has_contacts']=False
    contacts=dm_user.contacts.all()
    if list(contacts)<>[]:
      context['has_contacts']=True
    context['num_messages']=str(dm_user.num_messages)
    context['last_activity']=dm_user.last_activity 
    context['contacts']=contacts
    return ''

