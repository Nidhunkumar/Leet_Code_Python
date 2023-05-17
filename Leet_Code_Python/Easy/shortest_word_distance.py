'''
Given a list of words and two words word1 and word2, return the shortest distance between these two words in the list.

Example:
Assume that words = ["practice", "makes", "perfect", "coding", "makes"].

Input: word1 = “coding”, word2 = “practice”
Output: 3
Input: word1 = "makes", word2 = "coding"
Output: 1
Note:
You may assume that word1 does not equal to word2, and word1 and word2 are both in the list.
'''
import sys
def shortestDistance(words, word1, word2):
    if words == None or word1 == None or word2 == None:
        return -1

    idx1 = -1
    idx2 = -1
    minDiff = sys.maxsize

    for i in range(len(words)):
        if words[i] == word1:
            idx1 = i

        if words[i] == word2:
            idx2 = i

        if idx1 != -1 and idx2 != -1:
            minDiff = min(minDiff, abs(idx1 - idx2))

    return minDiff

lass Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        prev_w1, prev_w2 = -1, -1
        min_distance = len(words)

        for i in range(len(words)):
            if words[i] == word1:
                prev_w1 = i
                if prev_w2 != -1:
                    min_distance = min(min_distance, i - prev_w2)
            elif words[i] == word2:
                prev_w2 = i
                if prev_w1 != -1:
                    min_distance = min(min_distance, i - prev_w1)

        return min_distance
