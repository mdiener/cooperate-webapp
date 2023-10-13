# Cooperate Marketing Coding Challenge - Task 4: Demo App

## Setup

This is meant to be run in a virtual enviroment. As such please issue the following commands to setup and install all required dependencies:

### Linux
```
python -m venv .env
source .env/bin/activate
pip install -r requirements.txt
```

### Windows
```
python.exe -m venv .env
.\.env\Script\activate
pip install -r requirements.txt
```


## Run Web App

To run the webapp the following commands can be issues. Migrations are not necessary as it comes with a defined set of pre-existing users / data (can be extended on and edited). See further down for a fresh installation without pre-existing data.

```
cd cooperate
python manage.py runserver
```

### Default Superuser & Users

The following users and groups are created in the base database. By default a new user gets the `ad-viewer` permission. If a new `ad-manager` is requried, it can be changed through the admin interface.

#### Groups
* ad-viewer (can view ads)
* ad-manager (can manage ads)

#### Users

Admin user:
```
username: cooperate
password: marketing
```

Ad Viewer:
```
email: adviewer@example.org
password: test
```

Ad Manager:
```
email: admanager@example.org
password: test
```


### Fresh Installation without Data

To remove all data from the database and use a fresh installation, delete the file located at `cooperate/db.sqlite3` and issue the following commands:

```
cd cooperate
python manage.py migrate
python manage.py createsuperuser
```

Now you can run the command to start the server:

```
python manage.py runserver
```

For the app to properly work, please create the following groups with the following permissions:

#### ads-manager
  * can view ads
  * can create ads
  * can edit ads
  * can delete ads

#### ads-viewer
  * can view ads


## Future Work

While the app is working great, there are several things that could be imporved / added to.

### New Features

* Add the ability to remove and change ads through the manager interface.
* Allow sorting and filtering of ads when viewing them.
* Include a proper front end JavaScript library to allow more dynamic pages (probably React.js with Tailwind CSS).

### Improvements

* Automatically add the permission groups (with correct permissions and names) to the database when a clean install is done.
* Provide a simple form template to be used with all forms as opposed to rewriting the same code every time.
