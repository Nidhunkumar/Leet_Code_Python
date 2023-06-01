'''
346.moving average from data stream

Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

Sample I/O
Example 1
MovingAverage m = new MovingAverage(3);
m.next(1) = 1
m.next(10) = (1 + 10) / 2
m.next(3) = (1 + 10 + 3) / 3
m.next(5) = (10 + 3 + 5) / 3



'''
import collections
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.queue = collections.deque()
        self.size = size

    def next(self, val: int) -> float:
        if len(self.queue) == self.size:
            self.queue.popleft()
            self.queue.append(val)
        else:
            self.queue.append(val)
        return sum(self.queue)/len(self.queue)
    
