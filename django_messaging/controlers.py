import time

def time_to_duration(timestamp):
  #~ ztimeout = default number of minutes since user is considered as online
  ztimeout=4
  seconde=1
  minute=seconde*60
  jour=1440*minute
  nbjvisible=300000000
  timegmt=time.time()
  last_action=time.mktime(timestamp.timetuple())
  d=last_action-timegmt
  if -d/(60*60*24)<nbjvisible:
    if last_action+ztimeout*minute<float(timegmt):
      isoff=1;
    if d>-60:
      ff=str(int(d))+' sec'
    elif d>-60*60:
      ff=str(int(d/(60)))+' min'
    elif d>-60*60*24:
      ff=str(int(d/(60*60)))+' hrs'
    elif d>-60*60*30*24:
      ff=str(int(d/(60*60*24)))+' jour(s)'
    elif d>-60*60*30*24*12:
      ff=str(int(d/(60*60*24*30)))+' mois'
    else:
      ff=str(int(d/(60*60*24*30*12)))+' année(s)'
    return ff 
  return 'no'

"""
  #~ is user connected since few?
  lu=sequence.sort(env['root'].woo_info.users.objectValues(),(('last_connection', 'cmp', 'desc'),))
  luid=sequence.sort(env['root'].woo_info.users.objectIds(),(('last_connection', 'cmp', 'desc'),))
  for usr in lu:
    usrid=usr.getId()
    if usrid==env['user_id']:
      continue
    if usrid in my_friends_list:
      #~ check if user was not deleted
      user_exists=None
      if usrid not in luid:
        #oldlist=list(env['root'].woo_info.users[env['user_id']].contact_list)
        #newlist=oldlist.remove(usrid)
        #env['root'].woo_info.users[env['user_id']].manage_changeProperties(contact_list=newlist)
        msg.append('1')
      else:
        user_exists=1
        jour=1440*minute
        last_action=usr.last_connection
        d=float(last_action)-float(timegmt)
        if -d/(60*60*24)<nbjvisible:
          if float(last_action)+ztimeout*minute<float(timegmt):
            isoff=1;
          if d>-60:
            ff=str(int(d))+' '+lang[9]
          elif d>-60*60:
            ff=str(int(d/(60)))+' '+lang[10]
          elif d>-60*60*24:
            ff=str(int(d/(60*60)))+' '+lang[11]
          elif d>-60*60*30*24:
            ff=str(int(d/(60*60*24)))+' '+lang[12]
          elif d>-60*60*30*24*12:
            ff=str(int(d/(60*60*24*30)))+' '+lang[13]
          else:
            ff=str(int(d/(60*60*24*30*12)))+' '+lang[14]
      if user_exists:
        if not isoff:
          msg.append('<div class="df_friend_item">'+env['lib'].user_icon(usrid)+' <a href="javascript:send_pm(\''+usrid+'\')">'+usrid+'</a> <span class="df_last_connexion">'+ff+'</span></div>')
        else:
          msg.append('<div class="df_friend_item"> <img src="'+env['root_url']+'/woo_lib/images/pixel.gif" width="17" height="14" alt="" /> <a href="javascript:send_pm(\''+usrid+'\')">'+usrid+'</a> <span class="df_last_connexion">'+ff+'</span></div>')
"""
