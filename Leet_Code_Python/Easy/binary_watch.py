'''
401. Binary Watch
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".


Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must be consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".
 

Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]
Example 2:

Input: turnedOn = 9
Output: []


'''
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        output = []
        # Loop through all possible combinations of hours and minutes and count the number of set bits
        for h in range(12):
            for m in range(60):
                if bin(h).count('1') + bin(m).count('1') == turnedOn:  # Check if the number of set bits in hours and minutes equals the target number
                    output.append(f"{h}:{m:02d}")  # Add the valid combination of hours and minutes to the output list
        return output


#less time
class Solution:
    def nextBinary(self, current: int) -> int:
        if current == 0:
            return 0
        rightOne = current & -(current)
        nextHigherOneBit = current + int(rightOne)
        rightOnesPattern = current ^ int(nextHigherOneBit)
        rightOnesPattern = (int(rightOnesPattern) / int(rightOne))
        rightOnesPattern = int(rightOnesPattern) >> 2
        return nextHigherOneBit | rightOnesPattern


    def readBinaryWatch(self, turnedOn: int) -> List[int]:
        current = 2**turnedOn-1
        lowest = 63
        listTime=[]
        hours = 0
        if turnedOn == 0:
            return ["0:00"]
        while hours < 12:
            minutes = current & lowest
            hours = current >> 6
            if minutes<60 and hours <12:
                listTime.append(f'{hours}:{minutes:02}')
            current = self.nextBinary(current)
        return listTime
    
#less memory
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for i in range(2 ** 10):
            dcount = 0
            n = i
            mins = 0
            hours = 0
            for j in range(10):
                digit = n % 2
                dcount += digit
                if j < 6:
                    mins += 2 ** j * digit
                else:
                    hours += 2 ** (j - 6) * digit
                n = n // 2
            if dcount == turnedOn and mins < 60 and hours < 12:
                mstr = ("0" + str(mins))[-2:]
                result.append(str(hours) + ":" + mstr)
        return result
