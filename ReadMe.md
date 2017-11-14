## Test Service

A test service to play around with


### To Setup

```bash
virtualenv env -p python3
source env/bin/activate
pip install -r requirements.txt
```

### Run migrations

```bash
python manage.py migrate
```

### Create Super user

```bash
python manage.py createsuperuser
```

### Start Server

```bash
python manage.py runserver
```

A good place to start is http://localhost:8000/admin
login with your super user credentials