'''
387. First Unique Character in a String

Given a string s, find the first non-repeating character in it and return its index. If it does not exist, return -1.

 

Example 1:

Input: s = "leetcode"
Output: 0
Example 2:

Input: s = "loveleetcode"
Output: 2
Example 3:

Input: s = "aabb"
Output: -1

'''
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,c in enumerate(s):
            if s.count(c)==1:
                return i
                break
        return -1


#less time
class Solution:
    def firstUniqChar(self, s: str) -> int:
        minIdx=float('inf')
        for i in range(ord('a'),ord('z')+1):
            c = chr(i)
            idx=s.find(c)
            
            if idx!=-1 and idx==s.rfind(c):
                minIdx=min(minIdx,idx)
        
        
        if minIdx!=float('inf'):
            return minIdx 
        
        return -1

#less memory
class Solution:
    def firstUniqChar(self, s: str) -> int:
        abc = "abcdefghijklmnopqrstuvwxyz"
        ans = 10**5     # since 1 <= s.length <= 105, the answer must be smaller than 10^5
        print(s.find('e'))
        for c in abc:
            idx = s.find(c)     # check if this word is in s
            if (idx != -1 and idx == s.rfind(c)):   # check if first index == last index
                ans = min(ans, idx)     # store the smallest 
                
        return ans if ans < 10**5 else -1