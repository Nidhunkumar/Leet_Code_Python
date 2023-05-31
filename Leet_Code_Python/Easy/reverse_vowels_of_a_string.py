'''
345. Reverse Vowels of a String

Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"

'''
class Solution:
    def reverseVowels(self, s: str) -> str:
        loc=[]
        s=list(s)
        for i in range(len(s)):
            if(s[i] in "aeiouAEIOU"):
                loc.append(i)
        for i in range(len(loc)//2):
            s[loc[i]],s[loc[-i-1]]=s[loc[-i-1]],s[loc[i]]
        return "".join(s)

#less time

class Solution:
    def reverseVowels(self, s: str) -> str:
        word = list(s)
        vowels = set("aeiouAEIOU")

        l, r = 0, len(word)-1

        while l <= r:
            while l <= r and word[l] not in vowels: l += 1
            while l <= r and word[r] not in vowels: r -=1
            
            if l > r: break
            word[l], word[r] = word[r], word[l]
            l += 1
            r -= 1
        return "".join(word)

#less memory
class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel_str=""
        output=""
        for i in s:
            if i in "aeiouAEIOU":
                vowel_str+=i
        rev_vowel=vowel_str[::-1]
        x=0
        for i in s:
            if i in "aeiouAEIOU":
                output+=rev_vowel[x]
                x+=1
            else:
                output+=i
        return output

