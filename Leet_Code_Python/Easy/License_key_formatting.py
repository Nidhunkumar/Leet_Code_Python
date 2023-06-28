'''
482. License Key Formatting

You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.

We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.

Return the reformatted license key.

Example 1:

Input: s = "5F3Z-2e-9-w", k = 4
Output: "5F3Z-2E9W"
Explanation: The string s has been split into two parts, each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.
Example 2:

Input: s = "2-5g-3-J", k = 2
Output: "2-5G-3J"
Explanation: The string s has been split into three parts, each part has 2 characters except the first part as it could be shorter as mentioned above.

'''

class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
            # Remove dashes and convert lowercase letters to uppercase
        s = s.replace('-', '').upper()
        n = len(s)
    
    # Calculate length of first group
        first_len = n % k
    
    # Construct the reformatted license key
        reformatted = s[:first_len]
        for i in range(first_len, n, k):
            reformatted += '-' + s[i:i+k]
        
        if not reformatted:
            return ""
        elif reformatted[0] == "-":
            return reformatted[1:]
        else:
            return reformatted

#less time
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        groups = s.split("-")
        joined = "".join(groups)
        joined = joined.upper()

        start = len(joined) % k
        answer = joined[:start]

        for i in range(start, len(joined)-k+1,k):
            if i != 0:
                answer += "-"
            answer += joined[i:i+k]
        return answer


#less time
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:

        s = s.upper().replace('-', '')[::-1]
        res = ''

        while s != '':
            res += s[:k] + '-'
            s = s[k:]
        return res[:-1][::-1]




