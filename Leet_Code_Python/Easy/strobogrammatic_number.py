'''
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
Example 3:

Input: num = "962"
Output: false
Example 4:

Input: num = "1"
Output: true

'''
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        mapping = {"9": "6", "6": "9", "8": "8", "1": "1", "0": "0"}

        left = 0
        right = len(num) - 1
        
        while left <= right:
            if num[left] in mapping and mapping[num[left]] == num[right]:
                left += 1
                right -= 1            
            else:
                return False
        
        return True

class Solution:
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        l, r = 0, len(num) - 1
        while l < r:
            if num[l] == num[r] == '0': pass
            elif num[l] == num[r] == '8': pass
            elif num[l] == num[r] == '1': pass
            elif num[l] == '6' and num[r] == '9': pass
            elif num[l] == '9' and num[r] == '6': pass
            else: return False
            l += 1
            r -= 1

        if len(num) % 2 == 1: return num[len(num) // 2] in ('0', '8', '1')
        return True