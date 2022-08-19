init:
	docker-compose build
	docker-compose up -d

run:
	docker-compose exec python3 python src/generate.py

down:
	docker-compose down