'''
Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
'''
haystack = "sadbutsad"
needle = "sad"
class Solution:
    def __str__(self) -> str:
        pass
    def strStr(self, haystack: str, needle: str) -> int:
        index=-1
        for i in range(0,len(haystack)):
            strq=haystack[i:i+len(needle)]
            print(i)
            if strq==needle:
                index=i
                break
        return(index) 

print(haystack[0:9:3])


#less time
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)
    
#less memory
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle in haystack:
            return haystack.find(needle)
        else:
            return -1