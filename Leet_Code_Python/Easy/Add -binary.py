'''
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
'''


str(bin(int(a,2)+int(b,2)))[2:]


'''
less time
 if len(a)!=len(b):
            min_str = min((a, b), key=lambda x: len(x))
            max_str = max((a, b), key=lambda x: len(x))
            prepend = '0'*abs(len(a)-len(b))
            min_str = prepend+min_str
        else:
            min_str = a
            max_str = b
        carry = 0
        sum_result = deque()
        for chr1, chr2 in zip(min_str[::-1], max_str[::-1]):
            if chr1=='1' and chr2=='1':
                sum_result.appendleft(str(carry%2))
                carry = 1
            elif (chr1=='1' and chr2=='0') or (chr2=='1' and chr1=='0'):
                sum_result.appendleft(str((carry+1)%2))
            elif chr1=='0' and chr2=='0':
                sum_result.appendleft(str(carry%2))
                carry=0
        
        if carry == 1:
            sum_result.appendleft('1')
        
        return ''.join(list(sum_result))


less memory

  i, rest, sol, len_a, len_b = -1, 0, '', -len(a), -len(b)
        while i >= len_a or i >= len_b:
            a_bit = int(a[i]) if i >= len_a else 0
            b_bit = int(b[i]) if i >= len_b else 0
            sum = a_bit + b_bit + rest
            sol = str(sum % 2) + sol
            rest = sum // 2
            i -= 1
            
        return '1'+sol if rest else sol
        '''