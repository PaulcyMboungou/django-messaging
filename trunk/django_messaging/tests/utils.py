from django_messaging.models import DmUser, DmMessage
from django.contrib.auth.models import User

#~ shell functions to control the data
#users=User.objects.all()
#dm_users=DmUser.objects.all()
#dm_messages=DmMessage.objects.all()

#~ ============= users =============
def list_dm_users(dm_users):
  for dm_user in dm_users:
    print dm_user.user.username
  return

def list_users(users):
  for user in users:
    print user.username
  return

def check_all_users(users,dm_users):
  missing=[]
  dm_users_ids=[]
  for dm in dm_users:
    dm_users_ids.append(dm.user.id)
  for user in users:
    if user.id in dm_users_ids:
      print user.username+' has dm_user'
    else:
      missing.append(user.username)
  print '###### Users that do not have a dm_user: #####'
  print ' - '.join(missing)
  return

def create_all_dm_users(users,dm_users):
  dm_users_ids=[]
  for dm in dm_users:
    dm_users_ids.append(dm.user.id)
  for user in users:
    if user.id in dm_users_ids:
      print user.username+' already has dm_user'
    else:
      dm_user=DmUser(user=user)
      dm_user.save()
      print 'dm_user created for '+user.username
  return

