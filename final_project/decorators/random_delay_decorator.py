import time
import random


def random_delay(func):
    def wrapper(*args, **kwargs):
        delay_time = random.uniform(1, 3)
        time.sleep(delay_time)
        return func(*args, **kwargs)
    return wrapper