'''202. Happy Number
Easy
8.4K
1.1K
Companies
Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

 

Example 1:

Input: n = 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
Example 2:

Input: n = 2
Output: false'''

class Solution:
    def isHappy(self, n: int) -> bool:
        used = []
        while(n>0):
            tmp = 0
            while(n>0):
                i = n%10

                tmp += i*i
                n = n//10

            if(tmp in used):
                return False
            else:
                used.append(tmp)

            if(tmp==1):
                return True
            
            n = tmp

        return False

#less time
class Solution:
    def isHappy(self, n: int) -> bool:
        
        visited = set()
        curr_sum = 0
        while n > 0 and n not in visited and n != 1:
            visited.add(n)
            while n > 0:
                remainder = n%10
                curr_sum += (remainder*remainder)
                n = n//10
            n = curr_sum
            curr_sum = 0

    
        if n == 1:
            return True
        else:
            return False


#less memory
class Solution:
    def getSquaredSum(self,n):
        n = str(n)
        ans = 0
        for digit in n:
            ans += int(digit)**2
        return ans

    def isHappy(self, n: int) -> bool:
        htable = set()
        temp = n

        while True:
            temp = self.getSquaredSum(temp)
            if temp == 1:
                return True

            if temp in htable:
                return False
            else:
                htable.add(temp)

        return True




                  
        

