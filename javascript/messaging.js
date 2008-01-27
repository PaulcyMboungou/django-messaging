function load_index() {
  load_data("/messaging/","messaging");
  }

function load_contacts() {
  load_data("/messaging/contacts/","messaging");
  }
function popcontacts(mode) {
  var main=document.getElementById("df_main");
  var obj=document.getElementById("df_contacts_img");
  if (mode=="off") {
    main.style.height="auto";
    update_display('<a href="javascript:popcontacts('+"'on'"+')"><img src="woo_lib/images/icons/group.gif" title="Groups" alt="Groups" /></a>','df_contacts_img');
    load_friends();
    load_nummsg();
    }
  else {
    load_contacts();
    df_title=document.getElementById("df_title");
    df_title.innerHTML='Contacts';
    update_display('<a href="javascript:popcontacts('+"'off'"+')"><img src="woo_lib/images/icons/group.gif" title="Groups" alt="Groups" /></a>','df_contacts_img');
    }
  }
function add_contact(username) {
  url='woo_modules/directfriends/register_contact?username='+username;
  get_data(url,'df_main');
  }
function remove_contact(username) {
  url='woo_modules/directfriends/unregister_contact?username='+username;
  get_data(url,'df_main');
  }
function load_friends() {
   url='woo_modules/directfriends/load_friends';
   response=get_data(url,'df_main');
   update_display(response,'df_main')
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
   var url="woo_modules/directfriends/send_pm?user_id="+userid;
   var response=get_data(url,'df_main');
   update_display(response,'df_main');
   load_nummsg();
  }
function delete_pm(pmid) {
   var url="woo_modules/directfriends/delete_pm?pmid="+pmid;
   var response=get_data(url,'df_main');
   load_nummsg();
   load_msg_list('on');
  }
function send_pm_now(userid,pm) {
   url="woo_modules/directfriends/send_pm_process?to="+userid+"&pm="+pm;
   response=get_data(url,'df_main');
   url2='woo_modules/directfriends/load_friends';
   response2=get_data(url2,'df_main');
   update_display(response2,'df_main');
   load_nummsg();
  }
function load_nummsg() {
   url='woo_modules/directfriends/load_nummsg';
   response=get_data(url,'df_title');
   update_display(response,'df_title');
  }
function read_pm(pmid) {
   url='woo_modules/directfriends/read_pm?pmid='+pmid;
   response=get_data(url,'df_main');
   update_display(response,'df_main');
   load_nummsg();
  }
function read_first_pm() {
   url='woo_modules/directfriends/read_first_pm';
   response=get_data(url,'df_main');
   update_display(response,'df_main');
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

