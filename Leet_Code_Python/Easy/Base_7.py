'''
504. Base 7
Given an integer num, return a string of its base 7 representation.


Example 1:

Input: num = 100
Output: "202"
Example 2:

Input: num = -7
Output: "-10"


'''

class Solution:
    def convertToBase7(self, num: int) -> str:

        if num == 0: return '0'

        ans, n = '', abs(num)

        while n:
            n, m = divmod(n,7)
            ans+=str(m)

        if num < 0: ans+= '-'

        return ans[::-1]
    
#less time

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0: 
            return "0"
        a=""
        if num < 0:
            num = -num
            a = '-'
        ans = ""
        while num>0:
            ans += str(num % 7)
            num = num//7
        return a + ans[::-1]
    
#less memory

class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0:
            return str(num)
        negative_flag = False
        if num < 0:
            negative_flag = True
            num *= -1
        res = ""
        while num!= 0:
            res = str(num%7) + res
            num = num//7
        if negative_flag:
            res = "-" + res
        return res
        """
        # Solution 2 - recursive
        negative_flag = False
        if num < 0:
            negative_flag = True
            num *= -1
        if num == 0:
            return str(num)
        return self.convertToBase7(num//7) + str(num%7) + (
            ("-" if negative_flag else "")
        )
        """
        

