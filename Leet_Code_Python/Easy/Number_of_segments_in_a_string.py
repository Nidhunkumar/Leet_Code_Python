'''
434. Number of Segments in a String

Given a string s, return the number of segments in the string.

A segment is defined to be a contiguous sequence of non-space characters.

 

Example 1:

Input: s = "Hello, my name is John"
Output: 5
Explanation: The five segments are ["Hello,", "my", "name", "is", "John"]
Example 2:

Input: s = "Hello"
Output: 1

'''
class Solution:
    def countSegments(self, s: str) -> int:
        return len(s.split())

#less time
class Solution:
    def countSegments(self, s: str) -> int:
        s = s.strip()

        if len(s) == 0:
            return 0

        spaces = 0
        for i, char in enumerate(s):
            if s[i] == ' ' and i < len(s)-1 and s[i+1] != ' ':
                spaces += 1
        return spaces + 1

#less memory
class Solution:
    def countSegments(self, s: str) -> int:
        c=1
        d=""
        a=[]
        for i in range(len(s)):
            print(s[i])
            if s[i] !=" ":
                d+=s[i]
            else:
                if d!="":
                    a.append(d)
                d=""
        if d!="":
            a.append(d)
        return(len(a))
