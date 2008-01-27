from django.db import models
from django.contrib.auth.models import User

class DmUser(models.Model):
  user=models.ForeignKey(User,unique=True,related_name='dm_user')
  last_activity=models.DateTimeField(auto_now_add=True)
  num_messages=models.IntegerField(default=0)
  contacts=models.ManyToManyField(User,related_name='dm_contacts')

  #def is_online(self):

  #def is_alive(self):

  def get_messages(self):
    return DfMessage.objects.filter(user=self.user)

  def delete_message(self,message_id):
    msg=DmMessage.objects.get(id=message_id)
    msg.delete()
    #msg.save()
    return True
  
class DmMessage(models.Model):
  user=models.ForeignKey(DmUser)
  date=models.DateTimeField(auto_now_add=True)
  message=models.CharField(max_length=220)
