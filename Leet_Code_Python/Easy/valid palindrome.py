'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
'''
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Convert to lowercase and remove non-alphanumeric characters
        s = ''.join(c for c in s if c.isalnum()).lower()
        # Check if string is equal to its reverse
        return s == s[::-1]
    
#less time
class Solution:
    def isPalindrome(self, s: str) -> bool:
        forward_striped_s = [c for c in s.lower() if c.isalnum()]
        backward_striped_s = forward_striped_s[::-1]
        return forward_striped_s == backward_striped_s