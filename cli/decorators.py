import functools
from .utils import create_logs_dir


def log_info(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func(*args, **kwargs)
        create_logs_dir()
        with open("logs/info.txt", "a") as tf:
            tf.write(f"Function call: {func.__name__}\n")

    return wrapper
