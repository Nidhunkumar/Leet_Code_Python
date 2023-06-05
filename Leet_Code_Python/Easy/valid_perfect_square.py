'''
367. Valid Perfect Square

Companies
Given a positive integer num, return true if num is a perfect square or false otherwise.

A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.

You must not use any built-in library function, such as sqrt.

 
Example 1:

Input: num = 16
Output: true
Explanation: We return true because 4 * 4 = 16 and 4 is an integer.
Example 2:

Input: num = 14
Output: false
Explanation: We return false because 3.742 * 3.742 = 14 and 3.742 is not an integer.

'''

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l,r=1,num
        while l<=r:
            mid=(l+r)//2
            sqr=mid**2
            if sqr==num:
                return True
            if sqr<num:
                l=mid+1
            if sqr>num:
                r=mid-1
        return False



#less time

class Solution:
    # return int square or None if square is not integer

    def square(self, num: int) -> Optional[int]:
        
        if num == 0:
            return None
        elif num == 1:
            return 1
        
        # imaginary array [2,3,4,5...]. num = index + 2

        left = 0
        right = num - 3

        while left <= right:

            middle = left + (right - left) // 2
            middleNum = middle + 2
            middlePowed = middleNum * middleNum

            if middlePowed == num:
                return middleNum
            elif middlePowed > num:
                right = middle - 1
            else:
                left = middle + 1

        return None


    def isPerfectSquare(self, num: int) -> bool:

        s = self.square(num)
        
        return s is not None

#less memory
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        i = 1
        while i**2 <= num:
            if i**2 == num:
                return True
            i += 1

        return False

        