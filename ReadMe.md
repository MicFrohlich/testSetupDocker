## Test Service

A test service to play around with


### To Setup

```bash
docker-compose up -d
```
>This will run the entrypoint.sh on container startup

### Create Super user

```bash
docker exec -it <container> python manage.py createsuperuser
```

A good place to start is http://localhost:8000/admin
login with your super user credentials