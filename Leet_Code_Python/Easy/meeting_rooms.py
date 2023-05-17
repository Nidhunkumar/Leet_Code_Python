'''
252. Meeting Rooms (Python)

Description
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],…] (si < ei), determine if a person could attend all meetings.

Sample I/O
Example 1
Input: [[0,30],[5,10],[15,20]]
Output: false
Example 2
Input: [[7,10],[2,4]]
Output: true
'''
def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        new_intervals = sorted(intervals, key=lambda x: x[0])
        for i in range(1,len(new_intervals)):
            if new_intervals[i-1][1] > new_intervals[i][0]:return False
        return True


class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        def overlap(interval1: List[int], interval2: List[int]) -> bool:
            return (interval1[0] >= interval2[0] and interval1[0] < interval2[1]
                or interval2[0] >= interval1[0] and interval2[0] < interval1[1])
        #or
        #def overlap(interval1: List[int], interval2: List[int]) -> bool:
            #return  (min(interval1[1], interval2[1]) > max(interval1[0], interval2[0]))
        for i in range(len(intervals)):
            for j in range(i + 1, len(intervals)):
                if overlap(intervals[i], intervals[j]):
                    return False
        return True
