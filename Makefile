start:
    poetry run gunicorn --workers=4 --bind=127.0.0.1:5000 example.py:app


virtual:
	source venv/bin/activate

flask:
    flask --app example --debug run

# option + shift + F - autopep
