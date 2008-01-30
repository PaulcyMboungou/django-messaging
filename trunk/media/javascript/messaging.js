function load_index() {
  load_data("/messaging/","messaging");
  }

function load_contacts() {
  load_data("/messaging/contacts/","messaging_contacts");
  }

function pop_contacts(mode) {
  var main=document.getElementById("messaging_contacts");
  /* var obj=document.getElementById("messaging_contacts_icon"); */
  if (mode=="off") {
    main.style.height="auto";
    /* update_display('<a href="javascript:popcontacts('+"'on'"+')"><img class="icon" src="/site_media/icons/group.gif" title="Contacts" alt="Contacts" /></a>','messaging_contacts_icon'); */
    load_index(); 
    /* load_nummsg(); */
    }
  else {
    load_contacts();
    /* df_title=document.getElementById("df_title");
    #df_title.innerHTML='Contacts'; */
    update_display('<a href="javascript:pop_contacts('+"'off'"+')"><img class="icon" src="/site_media/icons/group.gif" title="Contacts" alt="Contacts" /></a>','messaging_contacts_icon');
    }
  }

function add_contact(contact_id) {
  load_data('/messaging/contacts/'+contact_id+'/add/','messaging_contacts');
  }

function remove_contact(contact_id) {
  load_data('/messaging/contacts/'+contact_id+'/remove/','messaging_contacts')
  }

function load_msg_list(mode) {
  var img='<img src="woo_lib/images/icons/mail_icon.gif" alt="Messages" title="Messages" />';
  var url_close_msg='<a href="javascript:load_msg_list('+"'off'"+')">'+img+'</a>';
  var url_open_msg='<a href="javascript:load_msg_list('+"'on'"+')">'+img+'</a>';
  if (mode=='on') {
    var url='woo_modules/directfriends/messages_list';
    var response=get_data(url,'df_main');
    update_display(response,'df_main');
    update_display(url_close_msg,'df_messages');
    load_nummsg();
    }
  else {
    load_nummsg();
    load_friends();
    update_display(url_open_msg,'df_messages');
    }
  }

function send_pm(userid) {
   var url="/messaging/send_pm/"+userid+'/';
   load_data(url,'messaging_contacts');
   load_nummsg();
  }

function delete_pm(pmid) {
   var url="woo_modules/directfriends/delete_pm?pmid="+pmid;
   var response=get_data(url,'df_main');
   load_nummsg();
   load_msg_list('on');
  }

function post_pm(userid,pm) {
   url="/messaging/post_pm/"+userid+"/?pm="+pm;
   load_data(url,'messaging');
  }

function load_nummsg() {
   url='/messaging/load_num_msgs/';
   load_data(url,'messaging_num_msgs');
  }

function read_pm(pmid) {
   url='woo_modules/directfriends/read_pm?pmid='+pmid;
   response=get_data(url,'df_main');
   update_display(response,'df_main');
   load_nummsg();
  }

function read_first_pm() {
   url='/messaging/read_first_pm/';
   load_data(url,'messaging_contacts');
   load_nummsg();
  }

function manage_contact(obj_ref,is_in_list) {
  var color="lime";
  var obj=document.getElementById(obj_ref);
  var df_switch=document.getElementById("df_switch");
  if (is_in_list=="yes") {
    obj.style.background="transparent";
    remove_contact(obj_ref);
    update_display('<a href="javascript:manage_contact('+"'"+obj_ref+"'"+",'no')"+'">[<span id="df_switch">+</span>] '+obj_ref+'</a>',obj_ref);
    }
  else {
    obj.style.background=color;
    add_contact(obj_ref);
    update_display('<a href="javascript:manage_contact('+"'"+obj_ref+"'"+",'yes')"+'">[<span id="df_switch">-</span>] '+obj_ref+'</a>',obj_ref);
    }
  }

