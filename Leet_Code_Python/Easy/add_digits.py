'''
258. Add Digits
Easy
4.1K
1.9K
Companies
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0



'''

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0 : return 0
        if num % 9 == 0 : return 9
        else : return (num % 9)

#less time

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0        # return zero
        elif num % 9 == 0:
            return 9        # return 9 when its totally divisible by 9 such that remainder is zero
        return num % 9      # return the remainder
    

#less memory
class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) > 1:
            sum: int = 0

            for i in range(len(str(num))):
                sum += (num % 10 ** (i + 1) - sum) // 10 ** i

            num = sum

        return num