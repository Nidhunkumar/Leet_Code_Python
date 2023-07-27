'''

557. Reverse Words in a String II

Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

 

Example 1:

Input: s = "Let's take LeetCode contest"
Output: "s'teL ekat edoCteeL tsetnoc"
Example 2:

Input: s = "God Ding"
Output: "doG gniD"
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([x[::-1] for x in s.split()])

#less time

class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()

        r = []

        for word in words:
            reversed_word = word[::-1]
            r.append(reversed_word)
        
        return ' '.join(r)

#less memory

class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        return " ".join(word[::-1] for word in l)

