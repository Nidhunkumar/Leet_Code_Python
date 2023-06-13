'''
405. Convert a Number to Hexadecimal

Given an integer num, return a string representing its hexadecimal representation. For negative integers, two’s complement method is used.

All the letters in the answer string should be lowercase characters, and there should not be any leading zeros in the answer except for the zero itself.

Note: You are not allowed to use any built-in library method to directly solve this problem.

 

Example 1:

Input: num = 26
Output: "1a"
Example 2:

Input: num = -1
Output: "ffffffff"

'''
class Solution:
  def toHex(self, num: int) -> str:
    # If the input number is zero, return '0'
    if num == 0:
        return '0'
    # If the input number is negative, convert it to its corresponding positive value using two's complement
    if num < 0:
        num = (1 << 32) + num
    
    hex_digits = '0123456789abcdef'  # The hexadecimal digits
    
    hex_num = ''  # Initialize an empty string to store the hexadecimal representation of the input number
    
    # Repeatedly divide the input number by 16 and convert the remainder to its corresponding hexadecimal digit until the quotient becomes zero
    while num > 0:
        digit = num % 16  # Get the remainder of dividing the input number by 16
        hex_digit = hex_digits[digit]  # Convert the remainder to its corresponding hexadecimal digit
        hex_num = hex_digit + hex_num  # Add the hexadecimal digit to the beginning of the hexadecimal representation
        num //= 16  # Update the input number by dividing it by 16
    
    return hex_num

#less time
class Solution:
    def toHex(self, num: int) -> str:
        n_bin = []
        n_hex = []
        n_hex_str = ""
        
        if not num:
            return '0'

        n_isneg = num < 0
        if n_isneg:
            num = num * -1
        
        if num == 2147483648:
            return "80000000"

        while num > 0:
            n_bin.insert(0, num%2)
            num = num//2
            
        print(n_bin,len(n_bin))
        if n_isneg:
            while len(n_bin) < 32:
                n_bin.insert(0,0)

            for i in range(len(n_bin)):
                n_bin[i] = 1 - n_bin[i]
            
            ind = 31
            add_flag = 0
            while not add_flag and ind:
                if n_bin[ind]:
                    n_bin[ind] = 0
                else:
                    n_bin[ind] = 1
                    add_flag = 1
                ind -= 1

        count = 0
        temp_hex = 0
        for b in n_bin[::-1]:
            temp_hex += b * (2**count)
            count += 1
            if count >= 4:
                count = 0
                n_hex.insert(0, temp_hex)
                temp_hex = 0

        if temp_hex:
            n_hex.insert(0,temp_hex)


        for h in n_hex:
            if h < 10:
                n_hex_str += str(h)
            else:
                n_hex_str += chr(ord('a') + h - 10)
    
        return n_hex_str
        
#less memory
HEX = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
class Solution:

    def toHex(self, num: int) -> str:
        if num < 0:
            # 2s complement
            num = 2**32 + num
        ans = []
        for i in range(8):
            n = num & 15
            
            #print(f"num={num}, n={n}")
            ans.insert(0, HEX[n])
            num = num >> 4
            if num == 0:
                break
        return "".join(ans)
    