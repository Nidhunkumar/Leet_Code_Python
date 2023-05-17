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
#  '''
# s = "()[]{"
# lookup={1:"(",2:")",3:"{",4:"}",5:"[",6:"]"}
# count=0
# l1=[]
# for i in s:
#    if i  in lookup.values():
#     l1.append(i)
# for j in l1:
#   if j in list(lookup.values()):
#     print(j)

# #print(l1)
'''Write a python program to print the count of strips/Line used to display a digit (Digits in Calculator Font).

For example :
Input - 123
Output - No. of strips Required : 12

'''
s="{})([]"
dict1 = {'(':')', '[':']', '{':'}'}
temp = []
for i in s:
          if i in dict1:
              temp.append(i)
          elif len(temp) == 0 or dict1[temp.pop()] != i:
              return False
      return len(temp) == 0


'''
less memory


  def isValid(self, s: str) -> bool:
        stack = []
        d = {')': '(', '}': '{', ']': '['}
        for i in s:
            if i in d:
                if stack and stack[-1] == d[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False

less time

 def isValid(self, s: str) -> bool:
        dict1 = {'(':')', '[':']', '{':'}'}
        temp = []
        for i in s:
            if i in dict1:
                temp.append(i)
            elif len(temp) == 0 or dict1[temp.pop()] != i:
                return False
        return len(temp) == 0




'''