import enum


class TimeUnit(enum.Enum):
    YEARS   = 1
    DAYS    = 2
    HOURS   = 3
    MINUTES = 4
    SECONDS = 5


class Duration():
    SINGULAR_TIME_UNITS = {
        TimeUnit.YEARS   : 'year',  
        TimeUnit.DAYS    : 'day',
        TimeUnit.HOURS   : 'hour',  
        TimeUnit.MINUTES : 'minute',
        TimeUnit.SECONDS : 'second'
    }

    PLURAL_TIME_UNITS = {
        TimeUnit.YEARS   : 'years',
        TimeUnit.DAYS    : 'days',
        TimeUnit.HOURS   : 'hours',
        TimeUnit.MINUTES : 'minutes',
        TimeUnit.SECONDS : 'seconds'
    }

    def __init__(self, amount, units):
        self.amount = amount
        self.units = units

    def __str__(self):
        if self.amount == 1:
            return '{} {}'.format(self.amount, self.SINGULAR_TIME_UNITS[self.units])
        else:
            return '{} {}'.format(self.amount, self.PLURAL_TIME_UNITS[self.units])

    def __repr__(self):
        return 'Duration({}, {})'.format(self.amount, self.units)

    def is_zero(self):
        return self.amount == 0

    def is_nonzero(self):
        return self.amount != 0


class Time():

    def __init__(self, seconds):
        seconds_remaining = seconds
        years = seconds_remaining // 31536000
        seconds_remaining %= 31536000

        days = seconds_remaining // 86400
        seconds_remaining %= 86400

        hours = seconds_remaining // 3600
        seconds_remaining %= 3600

        minutes = seconds_remaining // 60
        seconds_remaining %= 60

        self.time = { 
            TimeUnit.YEARS   : Duration(years, TimeUnit.YEARS),
            TimeUnit.DAYS    : Duration(days, TimeUnit.DAYS),
            TimeUnit.HOURS   : Duration(hours, TimeUnit.HOURS),
            TimeUnit.MINUTES : Duration(minutes, TimeUnit.MINUTES),
            TimeUnit.SECONDS : Duration(seconds_remaining, TimeUnit.SECONDS)
        }

    def is_zero(self):
        for value in self.time.values():
            if value.is_nonzero():
                return False

        return True

    def count_nonzeros(self):
        return len(list(filter(Duration.is_nonzero, self.time.values())))

    def __str__(self):
        if self.is_zero():
            return 'now'

        size = self.count_nonzeros()
        string = ''
        for i, duration in enumerate(filter(Duration.is_nonzero, self.time.values())):
            string += str(duration)
            if i == size - 2:
                string += ' and '
            elif i == size - 1:
                string += ''
            else:
                string += ', '

        return string


def format_duration(seconds):
    return str(Time(seconds))
