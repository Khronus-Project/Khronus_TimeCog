# Khron Us - Time Cog Library
## What is the Time Cog Library
- The Time Cog library aims to facilitate the management of time related data in solidity. 
- The library is built relying on conversion algorithms by Howard Hinnant documented at [Howard's Github Pages](https://howardhinnant.github.io/date_algorithms.html).
    - The algorithm based approach allows the functions to minimize gas consumption since it avoids running loops or lookup tables in solidity.
    - The library supports negative unix timestamps and negative time deltas, in the management of negative values the value doesn't rely on the casing of uint to int and viceversa which also, according to our testing, helps to reduce gas consumption.

## Offered Functionality
- Conversion between date formats, from date objects to day and unix timestamps and viceversa.
- Add units of time, minutes, hours, day and months, and get the resulting timestamp.
- Time Delta, substract one compared date from a base date.
- Next unit of time, get a rounded timestamp to the next Minute, Hour, Day or Month. 

## Installation
### Manual
- You can copy the library and deploy directly into your project.
### Brownie-ETH
- You can use the very convenient Brownie package manager to install directly from GitHub with the following command. 
    - Brownie PM Install Khronus-Project/Khronus_TimeCog@[version]
- Once the package is installed you can access the library by importing it to your contract with the following line.
    - ``import "Khronus-Project/Khronus_TimeCog@0.9.8/libraries/KhronusTimeCog.sol";``

## Conventions
- All internal utility functions of the library are marked as Private. These functions are internal to the algorithm and offer little to no value to be open for client contract execution.
- Functions might return more than one value. 
- Timestamps and time deltas can be negative, since it is cheaper to deal with integers than perform typecasting (according to our testing), the functions that might return a negative value return the timestamp and also a direction flag of 0 for positive, or 1 for negative values. Functions that return date objects also return several values but in this case the values are packed in an array of either 3 or 5 elements.
- When date objects are inputs, the convention is that each input year, month, day, is passed as standalone integers to allow readibility. The only exception is the timedaltes since two tuples of 3 integers would hamper instead of helping readibility.
- Valid dates are defined by default as between 1740 and 2200(exclusive), and the valid unix timestamps are from the first second of 1740 to the first second of 2200(inclusive). This keeps valid timestamps in tandem with valid dates. Since January first 2200 would be represented by 86400 different unix timestamps the conventions is that on the dates definition 2200 is an exclusive limit. In summary, January first 2200 is not valid as date, its day timestamp and its seconds representation are.
- Since negative numbers are managed as discussed above, when integers are mentioned in this document, unless, explicitely stated, we are refferring to unsigned integers.

## Detailed Function Information

### Convert Between Time Formats
- Date object to serial
    - Function Description
    ``getDayTimestamp(uint _year, uint _month, uint _day) public pure returns (uint _timestamp, uint _direction){}``
    - Inputs
        - Date object as three integers years, month, day
    - Outputs
        - Integer, TimeStamp in days
        - Integer, Direction 0 is positive 1 is negative
    - Function Call
    ``KhronusTimeCog.getDayTimestamp(uint _year, uint _month, uint _day)``

- Timestamp to object 
    - Long
        - Function Description
        ``getDateObject(uint _timestamp, uint _direction) public pure returns (uint[5] memory _result) {}``
        - Inputs
            - Integer, Unix timestamp in seconds
            - Integer, Direction 0 is positive 1 is negative
        - Outputs
            - Array of 5 Integers, year, month, day, hour, minute.
        - Function Call
        ``KhronusTimeCog.getDateObject(uint _timestamp, uint _direction)``
    - Short
        - Function Description
        ``getDateObjectShort(uint _timestampDays, uint _direction) public pure returns (uint[3] memory _result) {}`` 
        - Inputs 
            - Integer, Timestamp in days
            - Integer, Direction 0 is positive 1 is negative
        - Outputs
            - Array of 3 Integers, year, month, day.
        - Function Call
        ``KhronusTimeCog.getDateObjectShort(uint _timestampDays, uint _direction)``

### Add Time
- Functions
    - Add minutes 
    - Add hours
    - Add days
    - Add months
- Function Descriptions
    - ``function addMinutes(uint _timestamp, uint _minutes) public pure returns (uint _result) {}``
    - ``function addHours(uint _timestamp, uint _hours) public pure returns (uint _result) {}``
    - ``function addDays(uint _timestamp, uint _days) public pure returns (uint _result) {}``
    - ``function addMonths(uint _timestamp, uint _months) public pure returns (uint _result) {}``
- Inputs
    - Integer, Unix timestamp in seconds 
    - Integer, Units to add
- Outputs 
    - Integer, Unix timestamp in seconds
- Observations
    - Always exact, a minute add will always be rounded
- Function Calls
    - ``KhronusTimeCog.function addMinutes(uint _timestamp, uint _minutes)``
    - ``KhronusTimeCog.function addHours(uint _timestamp, uint _hours)``
    - ``KhronusTimeCog.function addDays(uint _timestamp, uint _days)``
    - ``KhronusTimeCog.function addMonths(uint _timestamp, uint _months)``

### Time Delta
- Function Description
``timeDelta(uint[3] memory _baseDate,uint[3] memory _comparedDate) public pure returns (uint _timestampDays, uint _direction){}``
- Inputs
    - Array of 3 integers (year, month, date) base date
    - Array of 3 integers (year, month, date) compared date
- Output 
    - Integer, Timestamp in days
    - Integer, Direction 0 is positive 1 is negative
- Function Call
```KhronusTimeCog.timeDelta(uint[3] memory _baseDate,uint[3] memory _comparedDate)``

### Next Unit of Time
- Functions
    - nextHour
    - nextDay
    - nextMonth
- Functions Description
    - ``function nextMinute(uint _timestamp) public pure returns (uint _result) {}``
    - ``function nextHour(uint _timestamp) public pure returns (uint _result) {}``
    - ``function nextDay(uint _timestamp) public pure returns (uint _result) {}``
    - ``function nextMonth(uint _timestamp) public pure returns (uint _result) {}``
-  Inputs
    - Integer, Unix timestamp in seconds 
- Outputs 
    - Integer, Unix timestamp in seconds
- Function Calls 
    - ``KhronusTimeCog.function nextMinute(uint _timestamp)``
    - ``KhronusTimeCog.nextHour(uint _timestamp)``
    - ``KhronusTimeCog.nextDay(uint _timestamp)``
    - ``KhronusTimeCog.nextMonth(uint _timestamp)``


## Tests
- A set of test dates are generated between the the first day of 1740 and 2200 (exclusive). There is one day picked at random from each year that is added to the test cases. A single year is picked at random in the range, the complete set of dates in this random picked year is also part of the test cases.
- These test cases are used for most of the test scenarios:
    - Time format conversion
    - Next time unit
    - Add Units of Time
    - For time deltas 100 hundreds test cases are picked at random from the date set described and they are tested as base and compared dates for the timedelta function.


## Gas Usage Estimation
- Below the gas consumption estimation provided by Brownie
### KhronusTimeCog 
|Function           | Gas Estimation AVG    | Gas Estimation Low | Gas Estimation High  |
|-------------------|-----------------------|--------------------|----------------------|
|timeDelta          | 30594  avg (confirmed)|  low:   30585      |   high:   30777      |
|addMonths          | 28339  avg (confirmed)|  low:   28171      |   high:   29098      |
|nextMonth          | 26870  avg (confirmed)|  low:   26860      |   high:   27027      |
|getDateObject      | 24984  avg (confirmed)|  low:   24973      |   high:   25061      |
|getDayTimestamp    | 24367  avg (confirmed)|  low:   24367      |   high:   24458      |
|getDateObjectShort | 24327  avg (confirmed)|  low:   24316      |   high:   24392      |
|addDays            | 22080  avg (confirmed)|  low:   22080      |   high:   22104      |
|addHours           | 22035  avg (confirmed)|  low:   22024      |   high:   22060      |
|addMinutes         | 22014  avg (confirmed)|  low:   22014      |   high:   22038      |
|nextDay            | 22002  avg (confirmed)|  low:   21994      |   high:   22006      |
|nextHour           | 21979  avg (confirmed)|  low:   21973      |   high:   21985      |
|nextMinute         | 21958  avg (confirmed)|  low:   21950      |   high:   21962      |