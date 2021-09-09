# Khron Us - Time Cog Library
## What is the Time Cog Library
- The Time Cog library aims to facilitate the management of time related data in solidity. 
- The library is built relying on conversion algorithms by Howard Hinnant documented at [Howard's Github Pages](https://howardhinnant.github.io/date_algorithms.html).
    - The algorithm based approach allows the functions to minimize gas consumption since it avoids running loops or lookup tables in solidity.
    - The library supports negative unix timestamps and negative time deltas, in the management of negative values the value doesn't rely on the casing of uint to int and viceversa which also, according to our testing, helps to reduce gas consumption.

## offered functionality
### Convert Between Time Formats



- Date object to serial
    - Inputs
        - Date object as three integers years, month, day
    - Outputs
        - TimeStamp in days
        - Direction 0 is positive 1 is negative

- Timestamp to object 
    - Long
        - Inputs
            - Unix timestamp in seconds
            - Direction 0 is positive 1 is negative
        - Outputs
            - Array of 5 Integers, year, month, day, hour, minute.
    - Short
        - Inputs 
            - Timestamp in days
            - Direction 0 is positive 1 is negative
        - Outputs
            - Array of 3 Integers, year, month, day.

### Add Time
- Functions
    - Add minutes 
    - Add hours
    - Add days
    - Add months
- Inputs
    - Unix timestamp in seconds 
    - Units to add
- Outputs 
    - Unixt timestamp in seconds
-Observations
    - Always exact, a minute add will always be rounded

### Next Unit of Time
- Functions
    - nextHour
    - nextDay
    - nextMonth
-  Inputs
    - Unix timestamp in seconds 
- Outputs 

### Time Delta
- Inputs
    - Array of 3 integers (year, month, date) base date
    - Array of 3 integers (year, month, date) compared date
- Output 
    - Timestamp in days
    - Direction 0 is positive 1 is negative

## Conventions
- All internal utility functions of the library are marked as Private. These functions are internal to the algorithm and offer little to no value to be open for client contract execution.
- Functions might return more than one value, timestamps and time deltas can be negative, since it is cheaper to deal with integers than perform typecasting (according to our testing), the functions that might return a negative value return the timestamp and also a direction flag of 0 for positive, or 1 for negative values. Functions that return date objects also return several values but in this case the values are packed in an array of either 3 or 5 elements.
- When date objects are inputs, the convention is that each input year, month, day, is passed as standalone integers to allow readibility. The only exception is the timedaltes since two tuples of 3 integers would hamper instead of helping readibility.
- Valid dates are defined by default as between 1740 and 2200(exclusive), and the valid unix timestamps are from the first second of 1740 to the first second of 2200(inclusive). This keeps valid timestamps in tandem with valid dates. Since January first 2200 would be represented by 86400 different unix timestamps the conventions is that on the dates definition 2200 is an exclusive limit. In summary, January first 2200 is not valid as date, its day timestamp and its seconds representation are.

## Tests
- A set of test dates are generated between the the first day of 1740 and 2200 (exclusive). There is one day picked at random for each year in that range in the testcases. A single year is picked at random in the range, the complete set of dates in this random picked year is also part of the test cases.
- These test cases are used for most of the test scenarios:
    - Time format conversion
        - ``getDayTimestamp(uint _year, uint _month, uint _day) public pure returns (uint _timestamp, uint _direction){}`
        - ``getDateObject(uint _timestamp, uint _direction) public pure returns (uint[5] memory _result) {}``
        - ``getDateObjectShort(uint _timestampDays, uint _direction) public pure returns (uint[3] memory _result) {}``
    - Next time unit
        - ``timeDelta(uint[3] memory _baseDate,uint[3] memory _comparedDate) public pure returns (uint _timestampDays, uint _direction){}``
        - ``function nextMinute(uint _timestamp) public pure returns (uint _result) {}``
        - ``function nextHour(uint _timestamp) public pure returns (uint _result) {}``
        - ``function nextDay(uint _timestamp) public pure returns (uint _result) {}``
        - ``function nextMonth(uint _timestamp) public pure returns (uint _result) {}``
    - Add Units of Time
        - ``function addMinutes(uint _timestamp, uint _minutes) public pure returns (uint _result) {}``
        - ``function addHours(uint _timestamp, uint _hours) public pure returns (uint _result) {}``
        - ``function addDays(uint _timestamp, uint _days) public pure returns (uint _result) {}``
        - ``function addMonths(uint _timestamp, uint _months) public pure returns (uint _result) {}``
    - For time deltas 100 hundreds test cases are picked at random from the date set described and they are tested as base and compared dates for the timedelta function.
        - ``timeDelta(uint[3] memory _baseDate,uint[3] memory _comparedDate) public pure returns (uint _timestampDays, uint _direction){}``
