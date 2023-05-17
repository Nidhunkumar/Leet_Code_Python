'''
232. Implement Queue using Stacks
Easy
6K
350
Companies
Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).

Implement the MyQueue class:

void push(int x) Pushes element x to the back of the queue.
int pop() Removes the element from the front of the queue and returns it.
int peek() Returns the element at the front of the queue.
boolean empty() Returns true if the queue is empty, false otherwise.
Notes:

You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 

Example 1:

Input
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 1, 1, false]

Explanation
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
'''
class MyQueue(object):
    def __init__(self):
        self.in_stk = []
        self.out_stk = []
	# Push element x to the back of queue...
    def push(self, x):
        self.in_stk.append(x)
	# Remove the element from the front of the queue and returns it...
    def pop(self):
        self.peek()
        return self.out_stk.pop()
	# Get the front element...
    def peek(self):
        if not self.out_stk:
            while self.in_stk:
                self.out_stk.append(self.in_stk.pop())
        return self.out_stk[-1]
	# Return whether the queue is empty...
    def empty(self):
        return not self.in_stk and not self.out_stk

#less time
class MyQueue:
    arr:list
    def __init__(self):
        self.arr = []

    def push(self, x: int) -> None:
        self.arr.append(x)

    def pop(self) -> int:
        return self.arr.pop(0)

    def peek(self) -> int:
        return self.arr[0]

    def empty(self) -> bool:
        return len(self.arr)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

#less memory
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.aux = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: void
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        while self.stack:
            self.aux.append(self.stack.pop())
        res = self.aux.pop()
        while self.aux:
            self.stack.append(self.aux.pop())
        return res
    
    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.stack[0]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return not self.stack

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()