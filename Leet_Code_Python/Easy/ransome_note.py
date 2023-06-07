'''
383. Ransom Note

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

 

Example 1:

Input: ransomNote = "a", magazine = "b"
Output: false
Example 2:

Input: ransomNote = "aa", magazine = "ab"
Output: false
Example 3:

Input: ransomNote = "aa", magazine = "aab"
Output: true

'''


magazine="aab"
ransomNote="aa"
class Solution:
  def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        my_map = {}
        for c in magazine:
            if c in my_map:
                my_map[c] += 1
            else:
                my_map[c] = 1
        for c in ransomNote:
            if c not in my_map or my_map[c] == 0:
                return False
            else:
                my_map[c] -= 1
        return True
  
#less time

class Solution:
    def canConstructCounter(self, ransomNote: str, magazine: str) -> bool:
        dic = {}
        for c in magazine:
            if c not in dic:
                dic[c] = 0
            dic[c] += 1
        for c in ransomNote:
            if c not in dic or not dic[c]:
                return False
            dic[c] -= 1
        return True

    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for c in set(ransomNote):
            if magazine.count(c) < ransomNote.count(c):
                return False
        return True
    
#less memory

from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note, mag = Counter(ransomNote), Counter(magazine)
        
        if note & mag == note: return True
        return False
       