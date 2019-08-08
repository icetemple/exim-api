import os


bind = 'unix:gunicorn.sock'
workers = os.getenv('GUNICORN_WORKERS', 1)
errorlog = '-'
reload = True
