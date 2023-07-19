'''
520. Detect Capital

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

 

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false

'''
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_capital=word.upper()
        all_small=word.lower()
        first_letter_capital=word.capitalize()

        if all_capital==word or all_small==word or first_letter_capital==word:
                return True
        else:
                return False

#less time

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper()==True or word.islower()==True or (word[0].isupper()==True and word[1:len(word)].islower()==True):
            return True
        else:
            return False
        
#less memory
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word[0].isupper() and word[1:].islower()


