'''Two Sum III - Data structure design
Design and implement a TwoSum class. It should support the following operations:addandfind.
add- Add the number to an internal data structure.
find- Find if there exists any pair of numbers which sum is equal to the value.
Example 1:
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
Example 2:
add(3); add(1); add(2);
find(3) -> true
find(6) -> false
'''
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        self.nums.append(number)
        

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        complements = set()
        for num in self.nums:
            if value - num in complements:
                return True
            
            complements.add(num)
            
        return False            

#Time Complexity: O(N).
#Space Complexity: O(N).




