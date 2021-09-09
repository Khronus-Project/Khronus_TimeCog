import pytest
from brownie import KhronusTimeCog_Test, accounts
from datetime import datetime, timezone
from dateutil.relativedelta import relativedelta
from random import randint
from utils import *

@pytest.fixture
def test_dates():
    return generate_dates(1740,2200)

@pytest.fixture
def khronus_times():
    time_cog = KhronusTimeCog_Test.deploy({'from':accounts[0]})
    return time_cog

### Time format conversion
####  ``getDayTimestamp(uint _year, uint _month, uint _day) public pure returns (uint _timestamp, uint _direction){}`
def test_getDayTimestamp(test_dates, khronus_times):
    for date in test_dates:
        test_day_timestamp = int(datetime.timestamp(date)/86400)
        case_expected_timestamp = abs(test_day_timestamp)
        if test_day_timestamp > 0:
            case_expected_direction = 0
        else:
            case_expected_direction = 1
        case_actual = khronus_times.getDayTimestamp(date.year,date.month,date.day)
        assert case_actual[0] == case_expected_timestamp and case_actual[1] == case_expected_direction  


####  ``getDateObject(uint _timestamp, uint _direction) public pure returns (uint[5] memory _result) {}``
def test_getDateObject(test_dates, khronus_times):
    for date in test_dates:
        test_timestamp = int(datetime.timestamp(date))
        if test_timestamp > 0:
            direction = 0
        else:
            direction = 1
        case_actual = khronus_times.getDateObject(abs(test_timestamp),direction) 
        assert case_actual[0] == date.year and case_actual[1] == date.month and case_actual[2] == date.day and case_actual[3] == date.hour and case_actual[4] == date.minute

####  ``getDateObjectShort(uint _timestampDays, uint _direction) public pure returns (uint[3] memory _result) {}``
def test_getDateObjectShort(test_dates, khronus_times):
    for date in test_dates:
        test_timestamp = int(datetime.timestamp(date)) / 86400
        if test_timestamp > 0:
            direction = 0
        else:
            direction = 1
        case_actual = khronus_times.getDateObjectShort(abs(test_timestamp),direction) 
        assert case_actual[0] == date.year and case_actual[1] == date.month and case_actual[2] == date.day

### Time delta
####  ``timeDelta(uint[3] memory _baseDate,uint[3] memory _comparedDate) public pure returns (uint _timestampDays, uint _direction){}``
def test_timeDelta(test_dates,khronus_times):
    cases = generate_time_delta_cases(test_dates,100)
    for case in cases:
        case_expected = time_delta(case["baseDate"],case["comparedDate"])
        case_actual = khronus_times.timeDelta([case["baseDate"].year,case["baseDate"].month,case["baseDate"].day],[case["comparedDate"].year,case["comparedDate"].month,case["comparedDate"].day])
        assert case_actual[0] == case_expected[0] and case_actual[1] == case_expected[1]  

### Next Rounded Unit
####  ``function nextMinute(uint _timestamp) public pure returns (uint _result) {}``
def test_nextMinute(test_dates, khronus_times):
    for date in test_dates:
        if date.year < 1970:
            pass
        else:
            testDateTime= date + relativedelta(seconds=+ randint(1,59))
            case_expected = int(datetime.timestamp(testDateTime + relativedelta(second=0, minutes=+1)))
            if case_expected <= 7258118400:
                case_actual = khronus_times.nextMinute(int(datetime.timestamp(testDateTime)))
                assert case_actual == case_expected
            else:
                try: 
                    case_actual = khronus_times.nextMinute(int(datetime.timestamp(testDateTime)))
                except Exception as e:
                    assert e.message == "VM Exception while processing transaction: Not a valid timestamp"

####  ``function nextHour(uint _timestamp) public pure returns (uint _result) {}``
def test_nextHour(test_dates, khronus_times):
    for date in test_dates:
        if date.year < 1970:
            pass
        else:
            testDateTime= date + relativedelta(seconds=+ randint(1,59), minutes=+ randint(1,59))
            case_expected = int(datetime.timestamp(testDateTime + relativedelta(second=0, minute=0, hours=+1)))
            if case_expected <= 7258118400:
                case_actual = khronus_times.nextHour(int(datetime.timestamp(testDateTime)))
                assert case_actual ==  case_expected 
            else:
                try: 
                    case_actual = khronus_times.nextHour(int(datetime.timestamp(testDateTime)))
                except Exception as e:
                    assert e.message == "VM Exception while processing transaction: Not a valid timestamp"

####  ``function nextDay(uint _timestamp) public pure returns (uint _result) {}``
def test_nextDay(test_dates, khronus_times):
    for date in test_dates:
        if date.year < 1970:
            pass
        else:
            testDateTime= date + relativedelta(seconds=+ randint(1,59), minutes=+ randint(1,59), hours=+ randint(1,23))
            case_expected = int(datetime.timestamp(testDateTime + relativedelta(second=0, minute=0, hour=0, days=+1)))
            if case_expected <= 7258118400:
                case_actual = khronus_times.nextDay(int(datetime.timestamp(testDateTime)))
                assert case_actual == case_expected
            else:
                try: 
                    case_actual = khronus_times.nextDay(int(datetime.timestamp(testDateTime)))
                except Exception as e:
                    assert e.message == "VM Exception while processing transaction: Not a valid timestamp"


####  ``function nextMonth(uint _timestamp) public pure returns (uint _result) {}``
def test_nextMonth(test_dates, khronus_times):
    for date in test_dates:
        if date.year < 1970:
            pass
        else:
            testDateTime= date + relativedelta(seconds=+ randint(1,59), minutes=+ randint(1,59), hours=+ randint(1,23))
            case_expected = int(datetime.timestamp(testDateTime + relativedelta(second=0, minute=0, hour=0, day=1, months=+1)))
            if case_expected <= 7258118400:
                case_actual = khronus_times.nextMonth(int(datetime.timestamp(testDateTime)))
                assert case_actual == case_expected 
            else:
                try: 
                    case_actual = khronus_times.nextMonth(int(datetime.timestamp(testDateTime)))
                except Exception as e:
                    assert e.message == "VM Exception while processing transaction: Not a valid timestamp"



### Add Units of Time
#### ``function addMinutes(uint _timestamp, uint _minutes) public pure returns (uint _result) {}``
def test_addMinutes(test_dates, khronus_times):
    for date in test_dates:
        if date.year < 1970:
            pass
        else:
            case_add_minutes = randint(0,1000)
            case_expected = int(datetime.timestamp(date + relativedelta(minutes=+ case_add_minutes)))
            if case_expected <= 7258118400:
                case_actual = khronus_times.addMinutes(int(datetime.timestamp(date)),case_add_minutes)
                assert  case_actual == case_expected 
            else:
                try: 
                    case_actual = khronus_times.addMinutes(int(datetime.timestamp(date)),case_add_minutes)
                except Exception as e:
                    assert e.message == "VM Exception while processing transaction: Not a valid timestamp"


#### ``function addHours(uint _timestamp, uint _hours) public pure returns (uint _result) {}``
def test_addHours(test_dates, khronus_times):
    for date in test_dates:
        if date.year < 1970:
            pass
        else:
            case_add_hours = randint(0,1000)
            case_expected = int(datetime.timestamp(date + relativedelta(hours=+ case_add_hours)))
            if case_expected <= 7258118400:
                case_actual = khronus_times.addHours(int(datetime.timestamp(date)),case_add_hours)
                assert case_actual == case_expected 
            else:
                try: 
                    case_actual = khronus_times.addHours(int(datetime.timestamp(date)),case_add_hours)
                except Exception as e:
                    assert e.message == "VM Exception while processing transaction: Not a valid timestamp"



#### ``function addDays(uint _timestamp, uint _days) public pure returns (uint _result) {}``
def test_addDays(test_dates, khronus_times):
    for date in test_dates:
        if date.year < 1970:
            pass
        else:
            case_add_days = randint(0,1000)
            case_expected = int(datetime.timestamp(date + relativedelta(days=+ case_add_days)))
            if case_expected <= 7258118400:
                case_actual = khronus_times.addDays(int(datetime.timestamp(date)),case_add_days)
                assert  case_actual == case_expected
            else:
                try: 
                    case_actual = khronus_times.addDays(int(datetime.timestamp(date)),case_add_days)
                except Exception as e:
                    assert e.message == "VM Exception while processing transaction: Not a valid timestamp"


#### ``function addMonths(uint _timestamp, uint _months) public pure returns (uint _result) {}``
def test_addMonths(test_dates, khronus_times):
    for date in test_dates:
        if date.year < 1970:
            pass
        else:
            case_add_months = randint(0,1000)
            case_expected = int(datetime.timestamp(add_months(date,case_add_months)))
            if case_expected <= 7258118400:
                case_actual = khronus_times.addMonths(int(datetime.timestamp(date)),case_add_months)
                assert case_actual == case_expected 
            else:
                try: 
                    case_actual = khronus_times.addMonths(int(datetime.timestamp(date)),case_add_months)
                except Exception as e:
                    assert e.message == "VM Exception while processing transaction: revert not a valid date as input as date object"

           