from .celery import app

@app.task
def modify_picture(*args, **kwargs):
    pass