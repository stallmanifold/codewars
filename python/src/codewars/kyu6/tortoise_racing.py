def race(v1, v2, g):
    if v1 >= v2:
        return None

    time     = 3600 * g // (v2 - v1)
    hours    = time // 3600
    seconds_remaining = time % 3600
    minutes  = seconds_remaining // 60
    seconds  = seconds_remaining % 60

    return [hours, minutes, seconds]
