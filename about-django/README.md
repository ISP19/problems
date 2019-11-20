# About Django

### Question
1.Explain how importance of settings.py file and what data contained in?

### Answer
It is very important because when you starts your project, everything in settings.py will be loaded which consist of your data such as database, installed applications, main URL as well as static files. So, when project run, it executes setting.py

### Question
2.How can we set up static files in django

### Answer
There are 3 main things that we need to do:
- set STATIC_ROOT in settings.py
- run manage.py collect static
- set up a Static Files entry on the PythonAnywhere web tab

### Question
3.Give 3 sample of django admin or command line of django and also specify their task

### Answer
1.django-admin migrate: Synchronizing the database state with the current set of models and migrations.
2.django-admin runserver:
Starting the development server.
3.django-admin version: Determining the version of Django
