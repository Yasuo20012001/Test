include .env

dev: stop start

stop:
	docker-compose down

start:
	docker-compose up -d --build
	docker-compose exec room_booking python manage.py migrate