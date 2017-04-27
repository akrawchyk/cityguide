export PATH := ./node_modules/.bin:$(PATH)
STATIC = cityguide/static
CSS = cityguide/css

.PHONY: collectstatics compile-css watch-css run install

collectstatics: compile-css
	python manage.py collectstatic --no-input

compile-css:
	suitcss --minify $(CSS)/cityguide.css $(STATIC)/cityguide.css

watch-css:
	suitcss --watch $(CSS)/cityguide.css $(STATIC)/cityguide.css

run:
	python manage.py runserver 0.0.0.0:8000

install:
	pipenv install
	npm install
