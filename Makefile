docker-up:
	docker-compose up --build -d
docker-down:
	docker-compose down
docker-exec:
	docker-compose exec app bash
create-su: # TODO: do something else to create superuser, this one returns error because of lack of 'username'
	@docker-compose exec app ./manage.py createsuperuser
