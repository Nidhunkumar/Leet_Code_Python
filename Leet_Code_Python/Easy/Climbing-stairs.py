'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
'''

def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(n):
            a, b = b, a + b
        return b


'''
less time
def util(n):
    if n == 0:
        return 1
    
    if n < 0:
        return 0
    
    if n in util.mem:
        return util.mem[n]
    
    util.mem[n] = util(n-1) + util(n-2)
    return util.mem[n]
    

class Solution:
    def climbStairs(self, n: int) -> int:
        util.mem = {}
        return util(n)
        


  less space
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        firstStep, secondStep, total = 1, 2, 0

        for i in range(3, n + 1):
            total = firstStep + secondStep
            firstStep = secondStep
            secondStep = total

        return total

'''