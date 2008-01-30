from django.db import models
from django.contrib.auth.models import User

class DmUser(models.Model):
  user=models.ForeignKey(User,unique=True,related_name='dm_user')
  last_activity=models.DateTimeField(auto_now_add=True)
  num_messages=models.IntegerField(default=0)
  contacts=models.ManyToManyField(User,related_name='dm_contacts')

  def get_messages(self):
    return DmMessage.objects.filter(user=self.user)

  def delete_message(self,message_id):
    msg=DmMessage.objects.get(id=message_id)
    msg.delete()
    return True

  def send_message(self,to_user,message):
    msg=DmMessage(from_user=self.user,user=to_user,message=message)
    msg.save()
    return True

  def has_message(self):
    msgs=self.get_messages()
    if list(msgs)<>[]:
      return True
    else:
      return False
  
class DmMessage(models.Model):
  user=models.ForeignKey(User)
  from_user=models.ForeignKey(User,related_name='from_user')
  date=models.DateTimeField(auto_now_add=True)
  message=models.CharField(max_length=255)
