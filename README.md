# Basic Flask Template

This is a template for a Flask web application with blueprints, authentication management, and a SQLite database. It provides a basic structure and functionality that can be customized to fit your specific needs.
Directory Structure

The directory structure for this template is as follows:

```
.
├── app.py
├── db.py
├── help
│   └── validators.py
├── models
│   └── User.py
├── routes
│   ├── account.py
├── static
│   ├── css
│   │   └── style.css
│   ├── js
│   │   └── app.js
│   └── media
│       └── flask-icon.png
├── templates
│   ├── account
│   │   ├── home.html
│   │   ├── sign_in.html
│   │   └── sign_up.html
│   ├── base.html
│   └── index.html
└── tests
    └── test_app.py
```

- `app.py`: the main Flask application file.
- `db.py`: contains functions for managing the SQLite database;
- `help`: contains helper files such as validators.py for input validation;
- `models`: contains database models such as User.py;
- `routes`: contains blueprint modules for different parts of the application such as account.py;
- `static`: contains static files such as CSS, JavaScript, and media files;
- `templates`: contains Jinja2 templates used to render HTML pages;
- `tests`: contains test files for your project. 

## Getting Started

1. Clone this repository or download the ZIP file and extract it to a directory of your choice.
2. Install the required dependencies by running the command:

    ```shell
    pip install -r requirements.txt
    ```

3. Modify the configuration variables in app.py to fit your needs. For example, you may want to change the **SECRET_KEY** variable to a different value.
4. Modify the database schema in models/User.py to fit your needs. You can also create additional models if necessary.
5. Modify the routes in routes/account.py to fit your needs. You can also create additional blueprint modules if necessary.
6. Run the application by running the command python app.py in your terminal.

## Run

### Tests
   ```shell
   python3 -m unittest discover -s tests
   ```

### Server
   ```shell
   python3 app.py
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
