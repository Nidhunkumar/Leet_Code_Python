'''
Given an integer x, return true if x is a 
palindrome, and false otherwise.

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.


Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Follow up: Could you solve it without converting the integer to a string?
'''

# def isPalindrome(x):
#         if x < 0:
#             return False
#         else:
#             x_str = str(x)
#             i = 0
#             j = len(x_str)-1
        
#             if j == 0:
#                 return True
        
#             while (x_str[i] == x_str[j]) and (i <= j):
#                 i = i + 1
#                 j = j - 1

#             if i < j:
#                 return False
#             else:
#                 return True

'''
Time: O(log x)
Space: O(log x)

 def isPalindrome(self, x: int) -> bool:
    if x < 0:
      return False

    rev = 0
    y = x

    while y:
      rev = rev * 10 + y % 10
      y //= 10

    return rev == x

code3(less time)

 def isPalindrome(x):
        old_x = str(x)
        new_x = old_x[::-1]
        return old_x == new_x
code4(less memory)
'''
x=121
def isPalindrome(x):
        z = str(x)
        y = list(str(x))
        y.reverse()
        print(y)
        y1 = "".join(y)
        print(y1)
        return(bool(z==y1))
isPalindrome(x)


# '''

            