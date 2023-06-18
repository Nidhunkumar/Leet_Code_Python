'''

415. Add Strings

Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"

'''
class Solution:
  def addStrings(self, num1: str, num2: str) -> str:
    # Reverse the input strings to start adding from the least significant digits
    num1 = num1[::-1]
    num2 = num2[::-1]
    # Pad the shorter input string with zeros
    if len(num1) < len(num2):
        num1 += '0' * (len(num2) - len(num1))
    else:
        num2 += '0' * (len(num1) - len(num2))
    
    result = ''
    carry = 0
    
    # Loop through both strings, starting from the least significant digits
    for i in range(len(num1)):
        # Convert the current digit in each string to an integer and add them together
        digit_sum = int(num1[i]) + int(num2[i]) + carry
        # Determine the carry for the next iteration, if any
        carry = digit_sum // 10
        # Append the least significant digit of the sum to the result string
        result += str(digit_sum % 10)
    
    # If there is a carry after the last iteration, append it to the result string
    if carry > 0:
        result += str(carry)
    
    # Reverse the result string to obtain the final sum
    return result[::-1]

#less time

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1 = num1[::-1]
        num2 = num2[::-1]
        # Pad the shorter input string with zeros
        if len(num1) < len(num2):
            num1 += '0' * (len(num2) - len(num1))
        else:
            num2 += '0' * (len(num1) - len(num2))
        
        result = ''
        carry = 0
        
        # Loop through both strings, starting from the least significant digits
        for i in range(len(num1)):
            # Convert the current digit in each string to an integer and add them together
            digit_sum = int(num1[i]) + int(num2[i]) + carry
            # Determine the carry for the next iteration, if any
            carry = digit_sum // 10
            # Append the least significant digit of the sum to the result string
            result += str(digit_sum % 10)
        
        # If there is a carry after the last iteration, append it to the result string
        if carry > 0:
            result += str(carry)
        
        # Reverse the result string to obtain the final sum
        return result[::-1]

#less memory
class Solution:
    def addStrings(self, n1: str, n2: str) -> str:
        m=len(n1)
        n=len(n2)
        if(m<n):
            n1,n2=n2,n1
            m,n=n,m
        i=m-1
        j=n-1
        c=0
        ans=""
        while(i>=0):
            k=int(n1[i])+c
            if(j>=0):
                k+=int(n2[j])
            if(k>9):
                c=1
                k=k%10
            else:
                c=0
            ans+=str(k)
            j-=1
            i-=1
        if(c==1):
            ans+="1"

        return ans[::-1]
            