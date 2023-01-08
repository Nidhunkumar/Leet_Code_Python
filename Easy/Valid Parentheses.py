'''

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
 '''
s = "()[]{"
lookup={1:"(",2:")",3:"{",4:"}",5:"[",6:"]"}
count=0
for i in s:
  if i  in lookup.values():
    print(i)
#print(count)