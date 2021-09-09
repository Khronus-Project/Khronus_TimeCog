from brownie import KhronusTimeCog, accounts
from datetime import datetime, timezone
from random import randint
from scripts.utils import *

def main():
    khronus_times = KhronusTimeCog.deploy({"from":accounts[0]})
    test_nextMonth(test_dates()[300:320], khronus_times)
    
def test_dates():
    return generate_dates(1740,2200)


def test_timeDelta(test_dates,khronus_times):
    cases = generate_time_delta_cases(test_dates,5)
    #cases = [{"baseDate":datetime(2021,9,7, tzinfo=timezone.utc),"comparedDate":datetime(2021,9,5, tzinfo=timezone.utc)}]
    for case in cases:
        caseExpected = time_delta(case["baseDate"],case["comparedDate"])
        caseExecuted = khronus_times.timeDelta([case["baseDate"].year,case["baseDate"].month,case["baseDate"].day],[case["comparedDate"].year,case["comparedDate"].month,case["comparedDate"].day])
        print(case["baseDate"], case["comparedDate"])
        print(caseExpected)
        print(caseExecuted)

def test_getDayTimestamp(test_dates, khronus_times):
    for date in test_dates:
        testvalues = khronus_times.getDayTimestamp(date.year,date.month,date.day)
        if testvalues[1] == 1:
            normalizer = -1
        else:
            normalizer = 1
        if date>datetime(2021,9,1, tzinfo=timezone.utc) and date < datetime(2021,9,10, tzinfo=timezone.utc):
            print (date)
            print(testvalues[0], (int(datetime.timestamp(date))/86400) * normalizer) 

def test_addMonths(test_dates, khronus_times):
    for date in test_dates:
        if date.year < 1970:
            pass
        else:
            case_I_add_months = randint(0,1000)
            case_I_expected = int(datetime.timestamp(add_months(date,case_I_add_months)))
            print(date, case_I_add_months, case_I_expected)
            if case_I_expected <= 7258118400:
                case_I_actual = khronus_times.addMonths(int(datetime.timestamp(date)),case_I_add_months)
            else:
                try: 
                    case_I_actual = khronus_times.addMonths(int(datetime.timestamp(date)),case_I_add_months)
                except Exception as e:
                    print(e.message)

def test_addHours(test_dates, khronus_times):
    for date in test_dates:
        if date.year < 1970:
            pass
        else:
            case_I_add_hours = randint(0,1000)
            case_I_expected = int(datetime.timestamp(date + relativedelta(hours=+ case_I_add_hours)))
            if case_I_expected <= 7258118400:
                case_I_actual = khronus_times.addHours(int(datetime.timestamp(date)),case_I_add_hours)
                print(date, case_I_add_hours)
                print(int(datetime.timestamp(date)), case_I_expected, case_I_actual, int((case_I_expected-case_I_actual)/3600), int((case_I_actual-int(datetime.timestamp(date)))/3600), int((case_I_expected - int(datetime.timestamp(date)))/3600) ) 
            else:
                try: 
                    case_I_actual = khronus_times.addHours(int(datetime.timestamp(date)),case_I_add_hours)
                except Exception as e:
                    print(e.message) 

def test_nextMonth(test_dates, khronus_times):
    for date in test_dates:
        if date.year < 1970:
            pass
        else:
            testDateTime= date + relativedelta(seconds=+ randint(1,59), minutes=+ randint(1,59), hours=+ randint(1,23))
            case_I_expected = int(datetime.timestamp(testDateTime + relativedelta(second=0, minute=0, hour=0, day=1, months=+1)))
            if case_I_expected <= 7258118400:
                case_I_actual = khronus_times.nextMonth(int(datetime.timestamp(testDateTime)))
                print(case_I_expected, case_I_actual, (case_I_actual-case_I_expected) % 86400, int((case_I_actual-case_I_expected)/ 86400 )) 
            else:
                try: 
                    case_I_actual = khronus_times.nextMonth(int(datetime.timestamp(testDateTime)))
                except Exception as e:
                    print(e.message)  
