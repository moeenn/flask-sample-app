PI = python
PIP = pip
APP = ./app
HOST = 0.0.0.0
PORT = 3000
ENTRYPOINT = wsgi:app
PROD_WORKERS = 4


# install project dependencies listed inside pyproject.toml file
install-deps:
	@echo "Installing server dependencies..."
	@${PIP} install .
	@echo "\n\nInstalling front-end dependencies..."
	@npm i -D


# run server in development mode i.e. with file reload / debug enabled
run-dev:
	dotenv flask --app ${ENTRYPOINT} run --host=${HOST} --port=${PORT} --debug


run-prod: 
	gunicorn ${ENTRYPOINT} --workers ${PROD_WORKERS} --bind 0.0.0.0:${PORT} --log-level info


shell:
	dotenv flask --app ${ENTRYPOINT} shell


db-init:
	dotenv flask --app ${ENTRYPOINT} db init


db-migrate:
	@echo "Generating migrations"
	dotenv flask --app ${ENTRYPOINT} db migrate
	@echo "\n\nApplying migrations"
	dotenv flask --app ${ENTRYPOINT} db upgrade


gen-secret:
	${PI} ${APP}/scripts/generate_secret.py
	

# run automated code tests
test:
	dotenv ${PI} -m unittest ${APP}/**/test_*.py


fmt:
	black ${APP}


lint:
	${PI} -m ruff check ${APP}


# recursively remove __pycache__ directories from project
clean:
	find . -type d -name  "__pycache__" -exec rm -r {} +
	rm -r .*_cache
	rm -r build
	rm -r *.egg-info
	