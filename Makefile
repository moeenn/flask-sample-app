PI = python
PIP = pip
APP = ./app
HOST = 0.0.0.0
PORT = 3000
ENTRYPOINT = wsgi:app
PROD_WORKERS = 4


# install project dependencies listed inside pyproject.toml file
install-deps:
	@echo "Installing project dependencies..."
	@${PIP} install .


# run server in development mode i.e. with file reload enabled
run-dev:
	dotenv flask --app ${ENTRYPOINT} run --host=${HOST} --port=${PORT} --debug


run-prod: 
	gunicorn ${ENTRYPOINT} --workers ${PROD_WORKERS} --bind 0.0.0.0:${PORT} --log-level info


# recursively remove __pycache__ directories from project
clean:
	find . -type d -name  "__pycache__" -exec rm -r {} +
	rm -r .*_cache
	rm -r build
	rm -r *.egg-info
	

# run automated code tests
test:
	dotenv ${PI} -m unittest ${APP}/**/test_*.py


fmt:
	black ${APP}


lint:
	${PI} -m ruff check ${APP}


assets-watch:
	npx tailwindcss -i ./app/static/src/global.css -o ./app/static/dist/global.css --watch


build:
	npx tailwindcss -i ./app/static/src/global.css -o ./app/static/dist/global.css
