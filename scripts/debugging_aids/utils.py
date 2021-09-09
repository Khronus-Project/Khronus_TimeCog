from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from random import randint

def generate_time_delta_cases(date_pool, case_number):
    cases = []
    for index in range (0,case_number):
        baseDate = date_pool[randint(0,len(date_pool)-1)]
        comparedDate = date_pool[randint(0,len(date_pool)-1)]
        if baseDate > comparedDate:
            direction = 0
        else:
            direction = 1
        cases.append ({"baseDate":baseDate, "comparedDate":comparedDate, "resultDirection":direction})
    return cases


def days_month(month):
    daysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return daysInMonth[month-1]

def generate_dates(start_year, end_year):
    test_dates = []
    for _year in range(start_year,end_year):
        _month = randint(1,12)
        _day = randint(1,days_month(_month))
        test_dates.append(datetime(_year,_month,_day, tzinfo=timezone.utc))
    _detailedYear = randint(start_year, end_year)
    for _month in range(1,13):
        for _day in range(1,days_month(_month)+1):
                test_dates.append(datetime(_detailedYear,_month,_day, tzinfo=timezone.utc))
    return test_dates

def time_delta(base_date, compared_date):
    delta = base_date - compared_date
    if delta.days < 0:
        direction = 1
    else:
        direction = 0
    return abs(delta.days), direction

def add_months(base_date, months_added):
    return base_date + relativedelta(months=+months_added)



 