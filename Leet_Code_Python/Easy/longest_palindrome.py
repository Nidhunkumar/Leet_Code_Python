'''
409. Longest Palindrome

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

 

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        odd_count = 0
        d = {}
        for ch in s:
            if ch in d:
                d[ch] += 1
            else:
                d[ch] = 1
            if d[ch] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
        if odd_count > 1:
            return len(s) - odd_count + 1
        return len(s)

#less time

class Solution:
    def longestPalindrome(self, s: str) -> int:
        count_of = Counter(s)
        oddCount = 0

        for letter in count_of.keys():
            #print(letter)
            if count_of[letter] % 2:
                oddCount += 1
        
        #print(oddCount, " ", count_of, len(s) - oddCount + 1)
        return len(s) - oddCount + 1 if oddCount else len(s)
        
#less memory
class Solution:
    def longestPalindrome(self, s: str) -> int:

        ss = set()
        for letter in s:
            if letter not in ss:
                ss.add(letter)
            else:
                ss.remove(letter)

        if len(ss) != 0:
            return len(s) - len(ss) + 1
        else:
            return len(s)

