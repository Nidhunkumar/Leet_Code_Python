'''
476. Number Complement
Easy
2.5K
116
Companies
The complement of an integer is the integer you get when you flip all the 0's to 1's and all the 1's to 0's in its binary representation.

For example, The integer 5 is "101" in binary and its complement is "010" which is the integer 2.
Given an integer num, return its complement.

 

Example 1:

Input: num = 5
Output: 2
Explanation: The binary representation of 5 is 101 (no leading zero bits), and its complement is 010. So you need to output 2.
Example 2:

Input: num = 1
Output: 0
Explanation: The binary representation of 1 is 1 (no leading zero bits), and its complement is 0. So you need to output 0.

'''

class Solution:
    def findComplement(self, num: int) -> int:
        return (int((bin(n)[2:]).replace('1', '2').replace('0','1').replace('2','0'),2))

        return (int((bin(n)[2:]).translate(str.maketrans("01", "10")),2))
    
#less time

class Solution:
    def findComplement(self, num: int) -> int:
        i: int = 1
        while i <= num:
            i <<= 1
        return i - num - 1
    
#less memory
class Solution:
    def findComplement(self, num: int) -> int:
        import math

        binary_digit = math.floor(math.log2(num))
        all_f = 2 ** (binary_digit + 1) - 1
        return num ^ all_f