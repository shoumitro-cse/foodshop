 #show all python package
 pip list


#install link => https://www.djangoproject.com/download/
#pip install Django
sudo pip install Django==3.0.1
python -m django --version


#django-admin startproject project_name_here   # create django project not recomended
python3 -m django startproject foodshop   # create django project
cd foodshop
python manage.py  runserver   #run server
python manage.py  runserver 0.0.0.0:8000
python manage.py  runserver 127.0.0.1:8000
python manage.py runserver 7000
http://127.0.0.1:8000/
python manage.py startapp user_account
python manage.py migrate       # create all database tables (must be use)
python manage.py createsuperuser  #create a super user
#http://127.0.0.1:8000/admin/
#shoumitro
#Bd12345678

#database shell
python manage.py dbshell

#Auto-generate the models from database each table
python manage.py inspectdb > custom_models.py    

#show only migrate sql    
python manage.py sqlmigrate public  0001_initial

#create models2.py file database tables
python manage.py makemigrations public --empty #Create an empty migration file.
python manage.py makemigrations # Create models file  myapp/migrations/0001_initial.py
python manage.py migrate  # create all database tables

#Django migrate : doesn't create tables 
python manage.py migrate -h
 python manage.py migrate --fake  public
 python manage.py migrate --fake public zero #Use the name "zero" to unapply all migrations.
 python manage.py migrate --run-syncdb
 
 #this 2 command is good
 python manage.py migrate --fake-initial public
 python manage.py migrate --fake-initial public  zero
 python manage.py migrate  # create all database tables 
 
 #migration database
 python manage.py migrate --database=sqilte_db
 python manage.py migrate --database=default

#for custom admin panel
#/usr/lib/python3.8/site-packages/django/contrib/admin/templates/admin/

#change default port
#/usr/lib/python3.8/site-packages/django/core/management/commands/runserver.py
    default_addr = '127.0.0.1'
    default_addr_ipv6 = '::1'
    default_port = '8000'
    protocol = 'http'
    server_cls = WSGIServer

# template syntax constants
#/usr/lib/python3.8/site-packages/django/template/base.py
FILTER_SEPARATOR = '|'
FILTER_ARGUMENT_SEPARATOR = ':'
VARIABLE_ATTRIBUTE_SEPARATOR = '.'
BLOCK_TAG_START = '{%'
BLOCK_TAG_END = '%}'
VARIABLE_TAG_START = '{{'
VARIABLE_TAG_END = '}}'
COMMENT_TAG_START = '{#'
COMMENT_TAG_END = '#}'
TRANSLATOR_COMMENT_MARK = 'Translators'
SINGLE_BRACE_START = '{'
SINGLE_BRACE_END = '}'



#for pdf view check (not require)
sudo pip install reportlab


#it is clean all cache file or image file under models
#django cleanup install
#https://github.com/un1t/django-cleanup
sudo pip install django-cleanup

#install django-cleanup => settings.py file
INSTALLED_APPS = [
    'django_cleanup.apps.CleanupConfig',
]

#check models under cleanup
from django.apps import apps
apps.get_models() #show all models that under cleanup

#refresh model 
from django_cleanup import cleanup
cleanup.refresh(model_instance)

#this model does not under cleanup
from django_cleanup import cleanup
@cleanup.ignore
class MyModel(models.Model):
    image = models.FileField()


#settings.py file change db name then require
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# for mysql
#https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database
#https://stackoverflow.com/questions/19189813/setting-django-up-to-use-mysql
# xampp : https://data-flair.training/blogs/django-database/
sudo pip install -U channels #install Django Channels
sudo pip install mysqlclient # it must be install otherwise it will be not work 
sudo pacman -S python-mysqlclient #not work bz not install mariadb
sudo pip install ConfigParser
sudo pip install MySQL-python

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'foodshop',
        'USER':'root',
        'PASSWORD':'',
        'HOST':'127.0.0.1',
        'PORT':'3306',
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",},
    }
}


#httpd.conf
#http://localhost/foodshop
WSGIPythonPath /opt/lampp/htdocs/foodshop/

Alias /static/ /opt/lampp/htdocs/foodshop/static/
Alias /media/ /opt/lampp/htdocs/foodshop/foodshop/media/

<Directory /opt/lampp/htdocs/foodshop/static>
    Require all granted
</Directory>

<Directory /opt/lampp/htdocs/foodshop/foodshop/media/>
    Require all granted
</Directory>

WSGIScriptAlias /foodshop /opt/lampp/htdocs/foodshop/foodshop/wsgi.py
<Directory /opt/lampp/htdocs/foodshop/foodshop>
	<Files wsgi.py>
		Order deny,allow
		Allow from all
	</Files>
</Directory>






