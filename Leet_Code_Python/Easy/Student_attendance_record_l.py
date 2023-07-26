'''
551. Student Attendance Record I

You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day. The record only contains the following three characters:

'A': Absent.
'L': Late.
'P': Present.
The student is eligible for an attendance award if they meet both of the following criteria:

The student was absent ('A') for strictly fewer than 2 days total.
The student was never late ('L') for 3 or more consecutive days.
Return true if the student is eligible for an attendance award, or false otherwise.

 

Example 1:

Input: s = "PPALLP"
Output: true
Explanation: The student has fewer than 2 absences and was never late 3 or more consecutive days.
Example 2:

Input: s = "PPALLL"
Output: false
Explanation: The student was late 3 consecutive days in the last 3 days, so is not eligible for the award.

'''

class Solution:
    def checkRecord(self, s: str) -> bool:
        A_count = 0
        L_count = 0
        for i in s:
            if i == "A":
                A_count += 1
                if A_count == 2:
                    return False
            if i == "L":
                L_count += 1
                if L_count > 2:
                    return False
            else:
                L_count = 0
        return True
    
#less time

class Solution:
    def checkRecord(self, s: str) -> bool:
        count = 0 
        
        for i in range(len(s)):
            if s[i] == 'A':
                count += 1 
            
            if i >= 2:
                if s[i] == s[i-1] == s[i-2] == 'L':
                    return False 
        
        return count < 2
        
#less memory

class Solution:
    def checkRecord(self, s: str) -> bool:
        return not ("LLL" in s or s.count('A') > 1)
