'''
680. Valid Palindrome II
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false

'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        count = 0
        if s == s[::-1]: return True
        while left < right:
            first, second = s[left], s[right]
            if first == second:
                left += 1
                right -= 1
            else:
                new1 = s[0:left] + s[left+1:]
                new2 = s[0:right] + s[right+1:]
                if new1 == new1[::-1]: return True
                elif new2 == new2[::-1]: return True
                else: return False
        return True

#less time

class Solution:
    def validPalindrome(self, s: str) -> bool:

        if s == s[::-1]: return True

        l, r = 0, len(s) - 1
        count = 0
        
        while s[l] == s[r]:
            l += 1
            r -= 1
        print(s[l:r], "one")
        print(s[l+1:r+1], "twi")
        newS = s[l + 1 : r + 1]
        if newS == newS[::-1]: return True

        newS = s[l: r]
        if newS == newS[::-1]: return True

        return False
    
#less memory
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return self.is_palindrome(s[l:r]) or self.is_palindrome(s[l+1:r+1])
            l += 1
            r -= 1
        return True
  
    def is_palindrome(self, s):
        l, r = 0, len(s) - 1
        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True
