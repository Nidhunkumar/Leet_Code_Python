'''
500. Keyboard Row
Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

 

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

'''

rows = (set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm"))

class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        
        return [w for w in words if any(set(w.lower()).issubset(row) for row in rows)]
    
#less time
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = (set("qwertyuiop"),set("asdfghjkl"),set("zxcvbnm"))
        return (w for row in rows for w in words if not set(w.lower()) - row )
    
#less memory
class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        l1=list('qwertyuiop')
        l2=list('asdfghjkl')
        l3=list('zxcvbnm')
        l=[]
        for i in words:
            l4=list(i)
            c1=0
            c2=0
            c3=0
            for j in i:
                s1=j.lower() in l1
                s2=j.lower() in l2
                s3=j.lower() in l3
                if(s1==True):
                    c1+=1
                elif(s2==True):
                    c2+=1
                elif(s3==True):
                    c3+=1
            if(c1==len(i)):
                l.append(i)
            elif(c2==len(i)):
                l.append(i)
            elif(c3==len(i)):
                l.append(i)
        return(l)
