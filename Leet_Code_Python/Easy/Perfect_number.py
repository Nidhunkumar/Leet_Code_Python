'''
507. Perfect Number

A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself. A divisor of an integer x is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return false.

 

Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
Example 2:

Input: num = 7
Output: false

'''

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # Check if num is less than 2 (no even perfect number exists)
        if num < 2:
            return False
        
        # Initialize the limit and the sum of divisors
        limit = int(num ** 0.5) + 1
        divisors_sum = 1
        
        # Iterate through the prime numbers up to the limit and calculate the sum of divisors
        for i in range(2, limit):
            if num % i == 0:
                divisors_sum += i
                if i != num // i:
                    divisors_sum += num // i
        
        # Check if num is equal to the sum of divisors
        if divisors_sum == num:
            return True
        else:
            return False
        
#less time
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        return num in [6,28,496,8128,33550336]

#less memory
class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        div = [1]
        for i in range(2, isqrt(num) + 1):
            if num % i == 0:
                div.append(i)
                div.append(num // i)
        #print(div)
        return sum(div) == num

