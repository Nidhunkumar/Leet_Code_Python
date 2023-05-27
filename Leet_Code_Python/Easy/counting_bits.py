'''
338. Counting Bits
Easy
8.8K
421
Companies
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

 

Example 1:

Input: n = 2
Output: [0,1,1]
Explanation:
0 --> 0
1 --> 1
2 --> 10
Example 2:

Input: n = 5
Output: [0,1,1,2,1,2]
Explanation:
0 --> 0
1 --> 1
2 --> 10
3 --> 11
4 --> 100
5 --> 101

'''

class Solution:
    def countBits(self, n: int) -> Iterable[int]:
        return map(int.bit_count, range(n + 1))

#less time   

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        offset = 1
        for i in range(1, n + 1):
            if offset*2 == i:
                offset *= 2
            res.append(1 + res[i - offset])
        return res
  
#less memory

class Solution:
    def countBits(self, n: int) -> List[int]:
        return map(lambda x: list(reversed(bin(x)[2:])).count('1'), range(0, n + 1))
    
    
    
