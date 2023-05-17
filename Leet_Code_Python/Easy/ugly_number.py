'''

263. Ugly Number

An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

Given an integer n, return true if n is an ugly number.

 

Example 1:

Input: n = 6
Output: true
Explanation: 6 = 2 * 3
Example 2:

Input: n = 1
Output: true
Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
Example 3:

Input: n = 14
Output: false
Explanation: 14 is not ugly since it includes the prime factor 7.

'''
class Solution:
    def isUgly(self, n: int) -> bool:
        while(n%2==0 and n!=0):
            n=n//2
        while(n%3==0 and n!=0):
            n=n//3
        while(n%5==0 and n!=0):
            n=n//5
        return(n==1)
    

#less time
class Solution:
    def isUgly(self, n: int) -> bool:
        if(n == 0): return False
        for x in [2, 3, 5]:
            while(n%x == 0):
                n = n//x
        return n==1

#less memory
class Solution:
    def isUgly(self, n: int) -> bool:
        if n <=1:
            return n>0
        for val in [2, 3, 5]:
            while n%val==0:
                n/=val
        return n==1