docker-up:
	docker-compose up --build -d
docker-down:
	docker-compose down
docker-exec:
	docker-compose exec app bash
lint:
	@docker-compose exec app pycodestyle ./src/ --exclude=./src/**/migrations/,./src/config/ --verbose
create-su:
	@docker-compose exec app ./manage.py csu
