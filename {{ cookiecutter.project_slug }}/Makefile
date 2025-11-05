
env:
	@source $(poetry env info --path)/bin/activate

install:
	poetry install

run:
	poetry run python -c "import django; django.setup(); print('Django OK')"

docs:
	poetry run mkdocs serve
