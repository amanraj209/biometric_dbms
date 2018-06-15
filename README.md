# Biometric DBMS

Biometric attendance system employs an automated system to calculate attendance of staff in an organisation and do further calculations of monthly attendance summary in order to reduce human errors in calculations.

## How to run
- `git clone https://github.com/amanraj209/biometric_dbms.git`.
- Install Python, Django.
- To migrate tables, run below commands
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py makemigrations biometric
$ python manage.py migrate biometric
```
- To start the server, run `python manage.py runserver`.
