from .celery import app


@app.task
def modify_picture(*args, **kwargs):
    pass


@app.task
def reverse(string):
    return string[::-1]