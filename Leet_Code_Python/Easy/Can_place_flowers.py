'''

605. Can Place Flowers

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty,
and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        c=0
        if n==0:
            return True
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                return True
            else:
                return False
        for i in range(len(flowerbed)):
            if i==0:
                if flowerbed[i]==0 and flowerbed[i+1]!=1:
                    flowerbed[i]=1
                    c+=1
            if i==len(flowerbed)-1:
                if flowerbed[i]==0 and flowerbed[i-1]!=1:
                    flowerbed[i]=1
                    c+=1
            if flowerbed[i]==1:
                continue
            else:
                if flowerbed[i-1]!=1 and flowerbed[i+1]!=1:
                    flowerbed[i]=1
                    c+=1
        if c>=n:
            return True
        else:
            return False
        
#less time 

class Solution:
    """
    Whether can plant flowers or not
    parameters:
        flowerbed: an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty
        n: the number of new flowers
    return: true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise
    """
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0:
            return True

        for i in range(len(flowerbed)):
            # check condition to plant new flowers
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
                # if n new flowers can be planted in the flowerbed, n == 0
                if n == 0:
                    return True

        return False

#less memory 

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        if n == 0: return True

        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed)-1):
            if flowerbed[i] == 1:
                continue
            if flowerbed[i-1] == flowerbed[i+1] == 0:
                n -= 1
                flowerbed[i] = 1
        return n <= 0