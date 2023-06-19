'''
422. Valid Word Square
Description

Given an array of strings words, return true if it forms a valid word square.

A sequence of strings forms a valid word square if the kth row and column read the same string, where 0 <= k < max(numRows, numColumns).

Example 1:


Input: words = ["abcd","bnrt","crmy","dtye"]
Output: true
Explanation:
The 1st row and 1st column both read "abcd".
The 2nd row and 2nd column both read "bnrt".
The 3rd row and 3rd column both read "crmy".
The 4th row and 4th column both read "dtye".
Therefore, it is a valid word square.
Example 2:


Input: words = ["abcd","bnrt","crm","dt"]
Output: true
Explanation:
The 1st row and 1st column both read "abcd".
The 2nd row and 2nd column both read "bnrt".
The 3rd row and 3rd column both read "crm".
The 4th row and 4th column both read "dt".
Therefore, it is a valid word square.
Example 3:


Input: words = ["ball","area","read","lady"]
Output: false
Explanation:
The 3rd row reads "read" while the 3rd column reads "lead".
Therefore, it is NOT a valid word square.

'''

class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                if i != j and (j >= len(words) or i >= len(words[j]) or words[i][j] != words[j][i]):
                    return False
            
        return True
#less time
#  
def validWordSquare(words):
    numRows = len(words)
    numColumns = len(words[0]) if words else 0

    # Check if the number of rows is equal to the number of columns
    if numRows != numColumns:
        return False

    # Check if each word[i][j] is equal to word[j][i]
    for i in range(numRows):
        for j in range(i, numColumns):  # Only iterate from i to numColumns
            if words[i][j] != words[j][i]:
                return False

    return True

    

def validWordSquare(words):
    numRows = len(words)
    numColumns = len(words[0]) if words else 0

    # Check if the number of rows is equal to the number of columns
    if numRows != numColumns:
        return False

    # Check if each word[i][j] is equal to word[j][i]
    for i in range(numRows):
        for j in range(numColumns):
            if words[i][j] != words[j][i]:
                return False

    return True
    
