'''

205. Isomorphic Strings

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

 

Example 1:

Input: s = "egg", t = "add"
Output: true
Example 2:

Input: s = "foo", t = "bar"
Output: false
Example 3:

Input: s = "paper", t = "title"
Output: true

'''
s='paper'
t='title'
e=len(set(s)) == len(set(zip(s, t))) == len(set(t))
print(len(set(zip(s, t))))

#less time
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap = {}
        mapchar = []
        index = 0 # mapchar index
        for i in range(len(s)):
            # if character not in hashmap -> add to hashtable
            if s[i] not in hashmap:
                # (No two characters may map to the same character)
                # if the map character already be used to map another character, return false
                if t[i] in mapchar:
                    return False
                # add new key to hashmap and add the map character of the key to mapchar
                # Ex: hashmap{e:0} ; mapchar[a]
                hashmap[s[i]] = index
                index += 1
                mapchar.append(t[i])
                continue
            
            # if the char will be replaced with not its map char, return false
            if mapchar[hashmap[s[i]]] != t[i]:
                return False

        return True
    
#less memory
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        '''
        title, paper
        12134  12134
        
        alg: one pointer, go through both words at once
        counting unique letters, saving a map
        '''
        letters = {}
        for i in range(len(s)):
            curr_s = s[i]
            curr_t = t[i]

            if curr_s not in letters:
                if curr_t in letters.values():
                    # letter mapping already in use
                    return False
                letters[curr_s] = curr_t

            elif letters[curr_s] != curr_t:
                # impossible letter mapping
                return False

        return True