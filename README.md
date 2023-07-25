# Room_Booking_test

## Technical Requirements for this Project:
Requirements:
* For rooms, there should be fields: number/name, price, capacity.
* Users should be able to filter and sort rooms by price and capacity.
* Users must be able to search for free rooms during a given time interval.
* Users must be able to book an available room.
* Superuser must be able to add/delete/edit rooms and edit booking records through the Django admin panel.
* Reservations can be canceled by both the user and the superuser.
* Users must be able to register and log in.
* Users must be logged in to book a room.
* Authorized users must see their reservations, while unregistered users can view rooms without login.
### Stack:
* Django;
* Django Rest Framework;
* PostgreSQL database is preferred, but not required.SQLite is also acceptable.



### This project was realized using the Django framework and the Django Rest Framework.

# Instruction:

* Before the first run, copy .env.dist to .env
* If necessary, change the configuration of ports, logins, passwords, etc.
* Download, install, and run Docker.
* Run the "make dev" command in the console.
* If you have Windows, run the following command instead: docker compose up -d --build

### Create a Super User for Both Services in Each Service Console with the Following Commands:

* For room_booking service in the terminal - python3 manage.py createsuperuser


### With the existing .env:

* Admin site link http://127.0.0.1:8001/admin/6
* Main page link http://127.0.0.1:8001/rooms/
* Reservations link http://127.0.0.1:8001/reservations/
* Login link http://127.0.0.1:8001/login/
* Register link http://127.0.0.1:8001/registration/

