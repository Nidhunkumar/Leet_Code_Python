'''
495. Teemo Attacking

Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, Ashe gets poisoned for a exactly duration seconds. More formally, an attack at second t will mean Ashe is poisoned during the inclusive time interval [t, t + duration - 1]. If Teemo attacks again before the poison effect ends, the timer for it is reset, and the poison effect will end duration seconds after the new attack.

You are given a non-decreasing integer array timeSeries, where timeSeries[i] denotes that Teemo attacks Ashe at second timeSeries[i], and an integer duration.

Return the total number of seconds that Ashe is poisoned.

 

Example 1:

Input: timeSeries = [1,4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 4, Teemo attacks, and Ashe is poisoned for seconds 4 and 5.
Ashe is poisoned for seconds 1, 2, 4, and 5, which is 4 seconds in total.
Example 2:

Input: timeSeries = [1,2], duration = 2
Output: 3
Explanation: Teemo's attacks on Ashe go as follows:
- At second 1, Teemo attacks, and Ashe is poisoned for seconds 1 and 2.
- At second 2 however, Teemo attacks again and resets the poison timer. Ashe is poisoned for seconds 2 and 3.
Ashe is poisoned for seconds 1, 2, and 3, which is 3 seconds in total.


'''

class Solution:
  def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
    if not timeSeries:
        return 0
    n = len(timeSeries)
    poisoned_time = 0
    
    for i in range(n-1):
        # calculate the duration of the poison effect
        duration_of_effect = min(duration, timeSeries[i+1]-timeSeries[i])
        poisoned_time += duration_of_effect
        
    # add the duration of the last poison effect
    poisoned_time += duration
    
    return poisoned_time

#less time
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        poisoned_start = timeSeries[0]
        poisoned_end = timeSeries[0] + duration
        poisoned_total = 0
        for time in timeSeries:

            if time <= poisoned_end:
                poisoned_total += (time - poisoned_start)
            else:
                poisoned_total += duration
            
            poisoned_start = time
            poisoned_end = poisoned_start + duration
        
        poisoned_total += duration
        return poisoned_total
                
#less memory
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        #poisoned_times = {t + x for x in range(duration) for t in timeSeries}

        poisoned_time = 0
        last_poisoned_time = -1
        remaining_times = timeSeries
        while len(remaining_times)>0:
            if last_poisoned_time >= remaining_times[0]:
                additional_time = remaining_times[0] + duration - last_poisoned_time
            else:
                additional_time = duration
            poisoned_time += additional_time
            last_poisoned_time = remaining_times[0] + duration
            remaining_times.pop(0)
            # remove all that have been eliminated other than last
            while len(remaining_times)> 1 and remaining_times[1] < last_poisoned_time:
                remaining_times.pop(0)

        return poisoned_time






        return len(poisoned_times)

