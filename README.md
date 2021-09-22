# A Django user management.

Custom user management.

## Screenshots

|     Home    |       Log In      |       Sign Up          |
| ------------|-------------------|------------------------|
| <img src="sample/index.png" width="200"> | <img src="sample/login.png" width="200"> | <img src="sample/signup.png"  width="200"> |


|      Log In  |    change email   |     Password change     |
| -------------|-------------------|-------------------------|
| <img src="sample/loggedin.png" width="200"> | <img src="sample/change_email.png" width="200"> | <img src="sample/change_password.png" width="200"> |


|            Profile update        |       Profile view     |
| ---------------------------------|------------------------|
| <img src="sample/profile1.png" width="200"> | <img src="sample/profile2.png" width="200"> |

## Functionality

- Log in
    - via username & password
    - via email & password
    - via email or username & password
    - with a remember me checkbox (optional)
- Create an account
- Log out
- Profile activation via email
- Reset password
- Remind a username
- Resend an activation code
- Change password
- Change email
- Change profile
- Multilingual: English, Amharic, Afaan Oromoo, Simplified Chinese

### Clone the project

```
git clone https://github.com/aliibsamohammed/customuser_management
cd customuser_management
```

### Install dependencies & activate virtualenv

```
pip install pipenv

pipenv install
pipenv shell
```

### Configure the settings (connection to the database, connection to an SMTP server, and other options)

1. Edit `customuser_project/customuser_project/conf/development.py` if you want to develop the project.

2. Edit `django_customuser/customuser_project/conf/production.py` if you want to run the project in production.

### Apply migrations

```
python customuser_project/manage.py migrate
```

### Collect static files (only on a production server)

```
python customuser_project/manage.py collectstatic
```

### Running

#### A development server

Just run this command:

```
python customuser_project/manage.py runserver
```
i n f o   a b o u t   t h i s   p r o j e c t  
 