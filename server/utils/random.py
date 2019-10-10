from datetime import timedelta
from random import randint, seed

seed(1)


def random_int_values(amount, min_value, max_value):
    result = []

    for _ in range(amount):
        result.append(randint(min_value, max_value))

    return result


def random_datetime_range(
    start, end, delta=timedelta(seconds=1), dt_format="%Y-%m-%d %H-%M-%S"
):
    result = []
    current = start

    while current < end:
        result.append(current.strftime(dt_format))
        current += delta

    return result
