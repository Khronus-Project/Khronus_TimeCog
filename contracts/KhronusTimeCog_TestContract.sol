// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/** 
 * @dev samples of imports using brownie and npm style (useful for remix) 
 * Khronus utilizes brownie as its development framework so all imports in sample contracts, test and auxiliary scripts keep Brownie-eth convensions.
 *  Brownie style import
 *      import "Khronus-Project/Khronus_TimeCog@1.0.3/libraries/KhronusTimeCog.sol"
 *  NPM install import (this can be used for remix)
 *      import "@khronus/time-cog@1.0.0/libraries/KhronusTimeCog.sol";
 **/

import "Khronus-Project/Khronus_TimeCog@1.0.3/contracts/src/KhronusTimeCog.sol";

contract KhronusTimeCog_Test {

    /*  
        This is a contract implementation aimed to allow the testing of the TimeCog library. 
    */

    //Get a timestamp in days since begining of unix epoch from a Civil Date to make it a Unix Timestamp multiply by number of seconds in day or solidity (1 days)
    function getDayTimestamp(uint _year, uint _month, uint _day) external pure returns (uint _timestamp, uint _direction){
       (_timestamp, _direction) = KhronusTimeCog.getDayTimestamp(_year, _month, _day);
    }
    
    //Get a Unix Timestamp from a full date-time object expressed as an array of 5 integers Year, Month, Day, Hour, Minute.
    function getDateObject(uint _timestamp, uint _direction) external pure returns (uint[5] memory _result) {
        _result = KhronusTimeCog.getDateObject(_timestamp, _direction);
    }
    
    //Get a day Timestamp from a full date object expressed as an array of 3 integers Year, Month, Day, to make it a Unix Timestamp multiply by number of seconds in day or solidity (1 days)
    function getDateObjectShort(uint _timestampDays, uint _direction) external pure returns (uint[3] memory _result) {
        _result = KhronusTimeCog.getDateObjectShort(_timestampDays, _direction);
    }
    
    //Time Delta
    function timeDelta(uint[3] memory _baseDate,uint[3] memory _comparedDate) external pure returns (uint _timestampDays, uint _direction){
        (_timestampDays, _direction) = KhronusTimeCog.timeDelta(_baseDate, _comparedDate);
    }

    //Next Unit of time, these functions return the unix timestamp of the next unit of time, the returned timestamp is always rounded to the 0 value.
    function nextMinute(uint _timestamp) external pure returns (uint _result) {
        _result = KhronusTimeCog.nextMinute(_timestamp);
    }

    function nextHour(uint _timestamp) external pure returns (uint _result) {
        _result = KhronusTimeCog.nextHour(_timestamp);
    }

    function nextDay(uint _timestamp) external pure returns (uint _result) {
        _result = KhronusTimeCog.nextDay(_timestamp);
    }

    
    function nextMonth(uint _timestamp) external pure returns (uint _result) {
        _result = KhronusTimeCog.nextMonth(_timestamp);
    }

    //Add Units of Time

    function addMinutes(uint _timestamp, uint _minutes) external pure returns (uint _result) {
        _result = KhronusTimeCog.addMinutes(_timestamp, _minutes);
    }

    function addHours(uint _timestamp, uint _hours) external pure returns (uint _result) {
        _result = KhronusTimeCog.addHours(_timestamp, _hours);
    }
    
    function addDays(uint _timestamp, uint _days) external pure returns (uint _result) {
        _result = KhronusTimeCog.addDays(_timestamp, _days);
    }

    function addMonths(uint _timestamp, uint _months) external pure returns (uint _result) {
        _result = KhronusTimeCog.addMonths(_timestamp, _months);
    }
    
    //utility functions for Civil Dates
    function isLeapYear(uint _year) external pure returns(bool _result) {
        _result = KhronusTimeCog.isLeapYear(_year);
    }
    
    function getDaysInMonth(uint _year,uint _month)external pure returns(uint _result) {
        _result = KhronusTimeCog.getDaysInMonth(_year, _month);
    }

    function isValidDate(uint _year, uint _month, uint _day) external pure returns(bool _result) {
        _result = KhronusTimeCog.isValidDate(_year, _month, _day);
    }

    function isValidTimestamp(uint _timestamp) external pure returns(bool _result) {
        _result = KhronusTimeCog.isValidTimestamp(_timestamp);
    }

    function isValidDayTimestamp(uint _timestamp) external pure returns(bool _result) {
        _result = KhronusTimeCog.isValidDayTimestamp(_timestamp);
    }

}