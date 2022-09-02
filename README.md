# *Project setup*
## *Linux*
```
$ git clone REPOSITORY_URL
$ cd FOLDER_NAME
$ python3 -m venv myenv
$ source myenv/bin/activate
$ pip3 install -r requirements.txt
```

*It should throw errors for database as we have not yet integrated database with it. So let's do that.*

*1. Install Postgres*

```
sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add 
sudo apt-get update
sudo apt-get -y install postgresql # You can define specific version here
```

*Please refer these links for more information*

    https://www.postgresql.org/download/linux/ubuntu/	
    https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-18-04

*2 .Creating a database*
* You should be able to create a database in postgres using create_db command, the database name you can keep it as you want. This database connection details is to be stored in .env file where we will store secrets. This file is in gitognore (What's the meaning of adding it in git, It's Top secret ;) )


*3 .Set Environment Variable*
- crete .env file as shown in .env-example

*4 .Migration*
```commandline
    python Manage.py makemigrations
    python manage.py migrate
```

*5 .For translation of static content*
 - Please follow below blog
 - https://testdriven.io/blog/multiple-languages-in-django/

*6 .To Automatically fill django.po file*
- use language_translate_script.py (not preferable may have fuzzy translation)

*7 .Run Below command in terminal*
- ```
    python manage.py runserver
  ```
- To shift from one language to another change language code (here en to fr)

*8 .For more detail*
- read all parts of this blog:https://fueled.com/blog/supporting-multiple-languages-in-django/





