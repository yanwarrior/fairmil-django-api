# App Name API

Welcome to `App Name` API. 
A backend application that provides a RESTFul API for `App Name` based on Django.  
We also provide a `User Interface` for the needs of clients or end users that you can access at:

- [App Name Web]()
- [App Name Mobile]()

## The main stacks
We built this on the following technology stacks:

- Python 3.6.8
- MariaDB (Server) 10.4.13
- Windows 7


### System Requirements

This application requires several packages such as:
- asgiref 3.2.10 or newer
- Django 3.0.8 or newer

> The application has been tested on Windows and 
> Linux operating systems based on the needs of the packages above.


## Quick Start

First, we strongly recommend that you use a virtual environment:

```
$ cd app_name
$ python -m venv .venv -p
```

Don't forget to activate the virtual environment:

```
$ source .venv/bin/activate
```

If you using windows:

```
.venv\Scrips\activate.bat
```

After that, run the following command to install the required packages:

```
pip install -r requirements.txt
```

Because we use the `MariaDB` database as default, please create a database with the name `db_app_name`.
Then, you can change it to add a `username` and `password` in the file `myproject/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'db_app_name',
        'USER': 'youruser',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

Next, you need to migrate:

```
python manage.py migrate
```

And make superuser:

```
python manage.py createsuperuser
```

Run the following command to run the development server:

```
python manage.py runserver
```

The API is ready and you can access it with:

```
http://localhost:8000/
```

For the `User Interface`, you can continue on the following link:

- [App Name Web]()
- [App Name Mobile]()

## Further help

- **Documentation**: we have provided a documentation of the features [here]() in PDF format.
- **App Demo**: For a demonstration, you can watch [this video]().
- **Installation Demo**: For installation, we also provide a [video for installation]().

