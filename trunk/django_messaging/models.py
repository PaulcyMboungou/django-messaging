from django.db import models
from django.contrib.auth.models import User

class DmUser(models.Model):
  user=models.ForeignKey(User,unique=True,related_name='dm_user')
  last_activity=models.DateTimeField(auto_now_add=True)
  num_messages=models.IntegerField(default=0)
  contacts=models.ManyToManyField(User,related_name='dm_contacts')

  def __unicode__(self):
    return self.user.username

  def get_messages(self):
    return DmMessage.objects.filter(user=self.user)

  def print_messages(self):
    msgs=DmMessage.objects.filter(user=self.user)
    for msg in msgs:
      print str(msg.id)+' - '+str(msg)
    if list(msgs)==[]:
      print 'No messages'
    return

  def delete_message(self,message_id):
    msg=DmMessage.objects.get(id=message_id,user=self.user)
    self.num_messages=self.num_messages-1
    print 'Deleting message '+str(msg)
    msg.delete()
    self.save()
    return True

  def delete_all_messages(self):
    msgs=self.get_messages()
    i=0
    for msg in msgs:
      print 'Deleting message '+str(msg)
      self.delete_message(msg.id)
      i=i+1
    print str(i)+' messages deleted'
    self.num_messages=0
    self.save()
    return 

  def send_message(self,to_user,message):
    msg=DmMessage(from_user=self.user,user=to_user,message=message)
    dm_user=DmUser.objects.get(user=to_user)
    dm_user.num_messages=dm_user.num_messages+1
    msg.save()
    dm_user.save()
    return True

  def has_message(self):
    if self.num_messages>0:
      return True
    return False

class DmMessage(models.Model):
  user=models.ForeignKey(User)
  from_user=models.ForeignKey(User,related_name='from_user')
  date=models.DateTimeField(auto_now_add=True)
  message=models.CharField(max_length=255)

  def __unicode__(self):
    return self.from_user.username+' -> '+self.user.username
