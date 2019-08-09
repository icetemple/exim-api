import os


bind = 'localhost:4000'
workers = os.getenv('GUNICORN_WORKERS', 1)
errorlog = '-'
reload = True
