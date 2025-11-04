from datetime import datetime


def get_timestamp():
    return datetime.now()


def get_elapsed_time(start, end):
    elapsed_time = end - start

    return elapsed_time
