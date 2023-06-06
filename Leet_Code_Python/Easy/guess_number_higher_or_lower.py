'''
374. Guess Number Higher or Lower

We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.

 

Example 1:

Input: n = 10, pick = 6
Output: 6
Example 2:

Input: n = 1, pick = 1
Output: 1
Example 3:

Input: n = 2, pick = 1
Output: 1

'''
class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l, r = 1, n
        while l < r:
            pass
def guess (n):
    """
    :type n: int
    :rtype: int
    """
    m=6
    if n > m:
        return -1
    elif n<m:
        return 1
    elif n==m:
        return 0


def guessNumber( n: int) -> int:
    l,r=1,n
    while l<r:
        mid=l+(r-l)//2
        if guess(mid)==0:
            return mid
        elif guess(mid)==-1:
            r=mid-1
        elif guess(mid)==1:
            l=mid+1


print(guessNumber(10))

#less time
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right)//2
            if guess(mid) < 1:
                right = mid
            else:
                left = mid + 1
        return left

#less memory

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        while l<=r:
            mid = (l+r)//2
            g = guess(mid)
            if g == 0:
                return mid
            if g==1:
                l = mid+1
            else:
                r=mid-1
        return l

