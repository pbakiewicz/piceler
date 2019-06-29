from celery import shared_task


@shared_task
def modify_picture(*args, **kwargs):
    pass


@shared_task
def reverse(string):
    return string[::-1]