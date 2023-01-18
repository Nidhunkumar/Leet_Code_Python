'''
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal 
substring
 consisting of non-space characters only.

 

Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
Example 2:

Input: s = "   fly me   to   the moon  "
Output: 4
Explanation: The last word is "moon" with length 4.
Example 3:

Input: s = "luffy is still joyboy"
Output: 6
Explanation: The last word is "joyboy" with length 6.
'''
s="luffy is still joyboy"

less time
s = list(s.rstrip().split())
print(len(s[-1]))
# less memory
 for i in range(len(s.split())):
            x1 = max(0, len(s.split()[i]) )
        return x1

# for word in s.split(' ')[::-1]:
#             if word != '':
#                 print(len(word))
# s=string.split()
# print(s)
# last_word=s[len(s)-1]
# print(last_word)
# print(len(last_word))