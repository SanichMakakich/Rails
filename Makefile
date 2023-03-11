start:
	flask --app example --debug run

virtual:
	source venv/bin/activate

gun:
    poetry run gunicorn --workers=4 --bind=127.0.0.1:5000 example.py:app

# option + shift + F - autopep
