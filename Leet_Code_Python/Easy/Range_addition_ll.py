'''
598. Range Addition II

You are given an m x n matrix M initialized with all 0's and an array of operations ops, where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.

Count and return the number of maximum integers in the matrix after performing all the operations.

 

Example 1:


Input: m = 3, n = 3, ops = [[2,2],[3,3]]
Output: 4
Explanation: The maximum integer in M is 2, and there are four of it in M. So return 4.
Example 2:

Input: m = 3, n = 3, ops = [[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3],[2,2],[3,3],[3,3],[3,3]]
Output: 4
Example 3:

Input: m = 3, n = 3, ops = []
Output: 9

'''


class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_y = m
        min_x = n

        for y, x in ops:
            min_y = min(min_y, y)
            min_x = min(min_x, x)

        return min_x * min_y
    
#less time
class Solution:            
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        mn_r,mn_c = m,n

        for r,c in ops:
            mn_r,mn_c = min(mn_r,r),min(mn_c,c)
        return mn_r*mn_c

#less memory

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        min_row , min_col = m , n
        for x,y in ops:
            min_row = min(min_row,x)
            min_col = min(min_col,y)
        return min_row * min_col    



