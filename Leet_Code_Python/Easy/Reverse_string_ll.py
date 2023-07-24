'''
541. Reverse String II

Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.

If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.

 

Example 1:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
Example 2:

Input: s = "abcd", k = 2
Output: "bacd"

'''

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        temp = []
        first = 0
        last = k-1                 
        while (first <= len(s)-1):     
            if last > len(s)-1:
                last = len(s) - 1
            while(last >= first): 
                temp.append(s[last])  
                last = last - 1
            first = first + k                 
            last = first + (k-1)
            while(last >= first):
                if first > len(s)-1:
                    break
                temp.append(s[first])  
                first = first + 1                
            last = first + (k-1)       
        return ''.join(temp)
            
#less time

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        p = 0
        while p < len(s):
            p2 = p+k
            s = s[:p] + s[p:p2][::-1] + s[p2:]
            p += 2*k
        return s




#less memory
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2*k):
            a[i:i+k] = reversed(a[i:i+k])
        return "".join(a) 
