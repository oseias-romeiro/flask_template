# Basic Flask Template

This is a template for a Flask web application with blueprints, authentication management, and a SQLite database. It provides a basic structure and functionality that can be customized to fit your specific needs.

- Try: [oseias-romeiro.alwaysdata.net/flask_template](http://oseias-romeiro.alwaysdata.net/flask_template/)

## Directory Structure

The directory structure for this template is as follows:

```
.
├── auth
│   └── loaders.py
├── app.py
├── controller
│   ├── account.py
├── config.py
├── models
│   └── User.py
├── static
│   ├── css
│   │   └── style.css
│   ├── js
│   │   └── app.js
│   └── media
│       └── flask-icon.png
├── templates
│   ├── account
│   │   ├── home.jinja2
│   │   ├── sign_in.jinja2
│   │   └── sign_up.jinja2
│   ├── base.jinja2
│   └── index.jinja2
└── tests
    └── test_app.py
```

- `auth`: contains modules to auth configuration
- `app.py`: the main Flask application file.
- `controller`: contains blueprint modules for different parts of the application such as account.py;
- `config.py`: config server and database getting env variables;
- `models`: contains database models such as User.py;
- `static`: contains static files such as CSS, JavaScript, and media files;
- `templates`: contains Jinja2 templates used to render HTML pages;
- `tests`: contains test files for your project. 

## Getting Started

1. Clone this repository or download the ZIP file and extract it to a directory of your choice.
2. Install the required dependencies by running the command:
    ```shell
    pip install -r requirements-{environment}.txt
    ```
    > if environment is prd (production) it is setup to mysql database

3. Modify the configuration variables in app.py to fit your needs. For example, you may want to change the **SECRET_KEY** variable to a different value.
4. Modify the database schema in models/User.py to fit your needs. You can also create additional models if necessary.
5. Modify the routes in routes/account.py to fit your needs. You can also create additional blueprint modules if necessary.
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

|username|email|password|
|--- |--- |--- |
|john|john@example.com|1234|
|jane|jane@example.com|1234|
|bob|bob@example.com|1234|

```shell
flask seed users
```


## Run

### Tests
   ```shell
   python3 -m unittest discover -s tests
   ```

### Server

- development environment

```shell
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

This template uses blueprints to organize the different parts of the application. Each blueprint module is responsible for a specific part of the application, such as authentication or user account management. This makes it easier to manage and scale the application as it grows.

### Authentication Management

This template includes a basic authentication management system using Flask-Login. Users can register for an account, log in, log out, and reset their password. Passwords are hashed and salted for security.

### SQLite Database

This template uses SQLite as the database management system. It includes a basic database schema for user accounts, but you can modify it to fit your specific needs. The db.py file contains functions for managing the database, such as creating tables and inserting data.

### Conclusion

This Flask template provides a basic structure and functionality for building a web application with blueprints, authentication management, and a SQLite database. It can be customized and expanded to fit your specific needs.
