'''
459. Repeated Substring Pattern

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.

'''
class Solution:
  def repeatedSubstringPattern(self, s: str) -> bool:
    # calculate the length of the string
    n = len(s)
    # try only those substring lengths that are factors of the length of the string
    for i in range(1, n // 2 + 1):
        if n % i == 0:
            # check only those substrings that start at the beginning of the string
            if s[:i] * (n // i) == s:
                return True
    
    return False
  
  #less time
  class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]
    
#less memory
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in s[1:] + s[:-1]
