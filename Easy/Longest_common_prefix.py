'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = 
Output: ""
Explanation: There is no common prefix among the input strings.
'''
strs =["flower","flow","flight"]











if not strs:
        print("none")
shortest = min(strs,key=len)
for i, ch in enumerate(shortest):
    for other in strs:
        if other[i] != ch:
            print(shortest[:i])
print( shortest )

#less time
pre = strs[0]
for i in strs:
    while not i.startswith(pre):
        pre = pre[:-1]

return pre

#less mem
res = ""
        
for i in range(0, len(strs[0])):
    for s in strs:
        if len(s) == i or s[i] != strs[0][i]:
            return res
        res += strs[0][i]
            
return res



