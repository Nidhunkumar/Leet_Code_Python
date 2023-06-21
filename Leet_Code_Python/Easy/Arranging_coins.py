'''
441. Arranging Coins

You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.

 

Example 1:


Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.
Example 2:


Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

'''
import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        ans = -0.5 + math.sqrt(1+8*n)/2
        return int(ans) 
    
#less time

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        while left <= right:
            middle = (left + right) // 2
            starsNeeded = (middle*(middle+1)) // 2
            if starsNeeded == n:
                return middle
            if starsNeeded > n:
                right = middle - 1
            else:
                left = middle + 1
        return right

#less memory
class Solution:
    def arrangeCoins(self, n: int) -> int:
        return int((math.sqrt(8*n + 1) - 1) / 2)
