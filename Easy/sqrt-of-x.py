'''
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
'''
import math
x=8
low=0
high=x
while True:
    n = low+(high-low)//2
    if n*n <= x <(n+1) * (n+1):
        print(n)
    elif x < n*n:
        high=n-1
    else:    
        low = n+1


'''
less time
i = 0
        j = int(x / 3)
        if j <= x:
            j = x + 1
                
        while True:
            k = int((j - i) / 4)
            if k < 1:
                k = 1
                
            print("f({},{},{})".format(i,j,k))
            
            for root in range(i, j, k):
                print("assert({}^2 >= {}) => {}".format(root,x,root**2>=x))
                
                if root * root == x:
                    return root
                elif root * root > x:
                    if k == 1:
                        return root - k

                    i = root - k
                    j = root + 1
                    break
                elif root + k >= j:
                    j += 1
'''