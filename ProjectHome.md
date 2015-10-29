A messaging system with users last activity indicator for the django framework. Good for community sites so people can see who is active, and communicate via quick pms.

The version 0.3 contains a few bugfixes, but it is still a beta.

## Features ##

  * Send personal messages to users that are in your contact list
  * Users see their contacts's last activity on the site in minutes/hours/days
  * Contact list management
  * Full ajax interface

![http://farm3.static.flickr.com/2411/2233080368_4a76546060.jpg](http://farm3.static.flickr.com/2411/2233080368_4a76546060.jpg)

## Install ##
This software works with django 0.97 svn

Put the folder django\_messaging in your python path
### Settings ###
Register the app: add this line in your INSTALLED\_APPS
```
'django_messaging',
```
Register the middleware: add this line in your MIDDLEWARE\_CLASSES
```
'django_messaging.middleware.DjangoMessagingMiddleware',
```
Configure the profile class:
```
AUTH_PROFILE_MODULE='django_messaging.DmUser'
```
Note: you have to use django\_messaging.DmUser class for the moment. The ability to use his own AUTH\_PROFILE\_MODULE class may be added later.

Be sure to have your MEDIA\_URL and MEDIA\_ROOT settings configured.

### Templates ###
Copy the templates/messaging folder to your templates directory.

Put this line in your template wherever you want the messaging interface to appear:

```
<p id="messaging"><script type="text/javascript">load_index()</script></p>
```

### Media files ###
Copy the media directory to the location setup in MEDIA\_ROOT and rename this directory to messaging

### Javascript ###
Add these lines to your main template to call the javascript libs (replace my\_media\_url with your media path):
```
<script type="text/javascript" src="my_media_url/messaging/javascript/ajax.js"></script>
<script type="text/javascript" src="my_media_url/messaging/javascript/messaging.js"></script>
```

## Setup ##

If you plug this module in a site that has existing users, you have to run a script before start using it, or adding users to contacts wont work until the users connect to the site:
  * Be sure to have your project in the python path
  * Export your settings environement variable (replace my\_project with your project name)
```
$ export DJANGO_SETTINGS_MODULE=my_project.settings
```
  * Run the setup script:
```
$ cd django_messaging/tests/
$ python setup.py
```

## Notes ##

The application is not yet internationalized: all the application messages are in french. Help welcome.

## Contribute and feedback ##

Please report any bugs

Feel free to improve the code or to come talk about the module: syntax\_error in #django-fr on irc.freenode.net - Site: http://www.patrainet.com