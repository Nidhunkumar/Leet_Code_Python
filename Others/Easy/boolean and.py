'''
Boolean and
Define a function named triple_and that takes three parameters and returns True only if they are all True and False otherwise.
'''
def triple_and(num1,num2,num3):
    ls=[num1,num2,num3]
    return all(ls)


def triple_and(a, b, c):
    return a and b and c

#print(triple_and(1,4,2))
