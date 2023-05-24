'''
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to compute all possible states of the string after one valid move.

For example, given s = "++++", after one move, it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]
If there is no valid move, return an empty list []
'''
class Solution:
    def canWin(self, s: str) -> bool:
        for i in range(1, len(s)):
            if s[i] == '+' and s[i - 1] == '+':
                if not self.canWin(s[:i - 1] + "--" + s[i + 1:]):
                    # Note: after flip, opponent cannot win, then player can win
                    return True
        return False

#############

'''
big-O analysis: (N!)

'''
class Solution(object):
  def canWin(self, s):
    """
    :type s: str
    :rtype: bool
    """

    def helper(s, visited):
      if s in visited:
        return visited[s]

      visited[s] = False
      for i in range(0, len(s) - 1):
        if s[i] + s[i + 1] == "++":
          if helper(s[:i] + "--" + s[i + 2:], visited) == False:
            visited[s] = True
      return visited[s]

    visited = {}
    return helper(s, visited)
