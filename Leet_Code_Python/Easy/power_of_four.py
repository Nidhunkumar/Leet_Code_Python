'''
342. Power of Four

Given an integer n, return true if it is a power of four. Otherwise, return false.

An integer n is a power of four, if there exists an integer x such that n == 4x.

 

Example 1:

Input: n = 16
Output: true
Example 2:

Input: n = 5
Output: false
Example 3:

Input: n = 1
Output: true

'''

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n==1:
            return True
        if n==0 or n%4!=0:
            return False
        return Solution.isPowerOfFour(self,n/4)
    
#less time
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        tmp = 1
        while tmp < n:
            tmp *= 4
        return tmp == n    
  
#less memory
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        step=1
        while step<n:
            step*=4
        return n==step