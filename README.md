# Room_Booking_test

## This is a technical requirements for this project:
Requirements:
* For rooms there should be fields: number/name, price, number, capacity.
* Users should be able to filter and sort rooms by price, by the capacity.
* Users must be able to search for free rooms at a given time interval.
* Users must be able to book an available room.
* Superuser must
* be able to add/delete/edit rooms, edit booking records through the Django admin panel.
* Reservations can be canceled by both the user and the superuser.
* Users must be able to register and log in.
* Users must be logged in to book a room.
* You can view rooms without login. Authorized users must see their reservations.
### Stack:
* Django;
* DRF;
* DB PostgreSQL preferred, but not required. The main thing is not SQLite;



### This project was realized with Django fraemwork and Django Rest Fraemwork.

# Instruction:

* Before the first run, you need to copy .env.dist to .env
* If necessary, change the configuration of ports, logins, passwords, etc.
* Download, install and run Docker
* Run "make dev" command in console
* If you have a Windows, then run the command instead of the previous command: docker compose up -d --build

### Create super user for both services in each service console with commands:

* for room_booking service in terminal - python3 manage.py createsuperuser


### With the existing .env

* admin site by the link http://127.0.0.1:8001/admin/6
* main page http://127.0.0.1:8001/rooms/
* reservations http://127.0.0.1:8001/reservations/
* login http://127.0.0.1:8001/login/
* register http://127.0.0.1:8001/registration/

