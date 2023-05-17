'''
Palindrome Permutation 
 We are given a string and asked if a permutation of the given string could form a palindrome.

Examples & Explanations
Example 1:

Input: s = "code"
Output: false
Explanation: we can not arrange letters of "code" to form a palindrome
Example 2:

Input: s = "aab"
Output: true
Explanation: permutation "aba" of given string is palindrome, hence true
Example 3:

Input: s = "carerac"
Output: true
Explanation: the given string is itself palindrome, there exists multiple permuations that form palindrome

'''
from collections import Counter

class solution:
    def can_form_palindrome(self,s):
      char_counts = Counter(s)
      odd_count = 0
      for count in char_counts.values():
          if count % 2 != 0:
              odd_count += 1
          if odd_count > 1:
              return False
      return True


from collections import defaultdict
class solution:
  def can_form_palindrome(self,s):
      char_freq = defaultdict(int)
      odd_count = 0
      # Count the occurrences of characters
      for char in s:
          char_freq[char] += 1
      # Count the odd frequencies
      for freq in char_freq.values():
          if freq % 2 != 0:
              odd_count += 1
          if odd_count > 1:
              return False
      return True

#less time

class solution:
    def can_form_palindrome(self,s):
      odd_chars = set()

      # Use a set to track characters with odd frequencies
      for char in s:
          if char in odd_chars:
              odd_chars.remove(char)
          else:
              odd_chars.add(char)

      # Check the size of the set
      if len(odd_chars) > 1:
          return False
      else:
          return True

