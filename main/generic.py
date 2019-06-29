from functools import partial
import os


def _update_filename(instance, filename, path):
    ext = filename.split('.')[-1]
    filename = f"{instance.name}.{ext}"

    return os.path.join(path, filename)


def upload_to(path):
    return partial(_update_filename, path=path)