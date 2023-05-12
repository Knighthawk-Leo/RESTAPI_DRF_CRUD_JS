# RESTAPI_DRF_CRUD_JS
# Django CRUD Operations Using PostgreSQL
This is a Django Rest Framwework API  performing CRUD operations using a PostgreSQL database



# Project Setup Instructions
Git clone the repository 
```
https://github.com/Knighthawk-Leo/RESTAPI_DRF_CRUD_JS.git
```
Configure the database / Settings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

```

 Make Migrations
```
py manage.py makemigrations
```
 Migrate Database
```
py manage.py migrate
```
 Run Project
```
py manage.py runserver
```
 Run Index.Html


Some Postman Screenshots 

![CRUD GET](https://github.com/Knighthawk-Leo/RESTAPI_DRF_CRUD_JS/blob/main/crud01.png)
![CRUD POST](https://github.com/Knighthawk-Leo/RESTAPI_DRF_CRUD_JS/blob/main/crud01.png)
