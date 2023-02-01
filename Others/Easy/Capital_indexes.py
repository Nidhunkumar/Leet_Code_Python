'''
Capital indexes
Write a function named capital_indexes. The function takes a single parameter, which is a string. Your function should return a list of all the indexes in the string that have capital letters.

For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].

'''
def capital_indexes(s):
    m=list(s)
    idx=[]
    lookup=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    for i,j in enumerate(m):
        if j.isupper():
            idx.append(i)
    return idx
            