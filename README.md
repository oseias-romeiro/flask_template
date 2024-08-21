# Flask Template

This project offers a well-structured template for building Flask applications that include a robust authentication system and fine-grained role permissions control. It provides a best-practice foundation for Flask development, integrating essential extensions such as Flask-Login for user session management, Flask-WTF for form handling and CSRF protection, Flask-SQLAlchemy for database management, and Flask-Migrate for seamless database migrations. This template is designed to streamline development and ensure that your Flask applications are built on a solid, scalable, and secure foundation.

## Directory Structure

The directory structure for this template is as follows:

```
.
├── app.py
├── auth
│   ├── loaders.py
├── cli_cmds.py
├── config.py
├── controller
│   ├── account.py
├── forms
│   ├── AuthForm.py
├── middleware
│   └── wraps.py
├── models
│   └── User.py
├── requirements.txt
├── routes
│   ├── account.py
│   ├── admin.py
│   ├── public.py
├── seeds
│   └── users.json
├── static
│   ├── css
│   │   └── style.css
│   ├── js
│   │   └── app.js
│   └── media
│       ├── flask-icon.png
│       └── flask-logo.png
├── templates
│   ├── account
│   │   ├── change_password.jinja2
│   │   ├── delete.jinja2
│   │   ├── home.jinja2
│   │   └── profile.jinja2
│   ├── admin
│   │   └── panel.jinja2
│   ├── base.jinja2
│   ├── error
│   │   └── 404.jinja2
│   ├── forgot_password.jinja2
│   ├── index.jinja2
│   ├── sign_in.jinja2
│   └── sign_up.jinja2
├── tests
│   ├── test_routes.py
│   ├── test_signin.py
│   └── test_signup.py
└── wsgi.py
```

- `auth`: modules to auth configuration;
- `app.py`: the main Flask application file;
- `cli_cmds.py`: setup cli commands;
- `config.py`: config server and database getting env variables;
- `controller`: modules with functions to proccessing and interact with database;
- `forms`: defined forms for rendering and validation;
- `middleware`: wraps to encapsulate routes;
- `models`: database models;
- `routes`: blueprint modules for different parts of the application such as account.py;
- `seeds`: intial data to feed database;
- `static`: static files such as CSS, JavaScript, and media files;
- `templates`: Jinja2 templates used to render HTML pages;
- `tests`: unit tests for project;
- `wsgi.py`: config gateway interface.

## Getting Started

1. Clone this repository or download the ZIP file and extract it to a directory of your choice.
2. Install the required dependencies by running the command:
    ```shell
    pip install -r requirements.txt
    ```
    > if environment is prd (production) it is setup to mysql database

3. Modify the environment variable in `.env` to fit your needs. You need set the **SECRET_KEY**. Check [.env.example](.env.example) file
4. Modify the database schema in models/User.py to fit your needs. You can also create additional models if necessary.
5. Modify the routes and controllers to fit your needs. You can also create additional blueprint modules if necessary.
6. Setup database and use the seeds (see [Setup](#setup))
7. Run the application by running the command `flask run` in your terminal.

## Setup

```shell
flask db init
flask db migrate -m "init"
flask db upgrade
```

### Seeds
Insert data in database, defined in [seed.py](./seed.py)

|username|email|password|role|
|--- |--- |--- | ---|
|john|john@example.com|1234|USER|
|jane|jane@example.com|1234|USER|
|bob|bob@example.com|1234|ADMIN|

```shell
flask seed users
```

> Do not use in production environment

## Run

### Tests
Setup database before and running tests:

   ```shell
   python3 -m unittest discover -s tests
   ```

### Server

- development environment

```shell
export FLASK_DEBUG=yes
flask run
```
> Access [localhost:5000](http://localhost:5000)

- production evironment

```sh
gunicorn -b 0.0.0.0:80 wsgi:app
```

> Access [localhost](http://localhost)

## Docker
```shell
docker build . -t flask_template
docker run -d --name flask_template -p 5000:80 flask_template
```

## Features

### Blueprints

This template uses blueprints to organize the different parts of the application. Each blueprint module is responsible for a specific part of the application, such as authentication, user account management and admin control. This makes it easier to manage and scale the application as it grows.

### Authentication and Role Management

This template includes a basic authentication management system using Flask-Login. Users can register for an account, log in, log out, change profile data and reset their password. Passwords are hashed and salted for security. Furthermore, is used roles to restrict access to users and give permissions to each one.

### Database

This template uses SQLite as the database management system for default in development and test environments, but you can change this in [config.py](./config.py). It includes a basic database schema for user accounts, but you can modify it to fit your specific needs.

### Conclusion

This Flask template provides a basic structure and functionality for building a web application with blueprints, authentication management, and a SQLite database. It can be customized and expanded to fit your specific needs.
