"""
412. Fizz Buzz

Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
 

Example 1:

Input: n = 3
Output: ["1","2","Fizz"]
Example 2:

Input: n = 5
Output: ["1","2","Fizz","4","Buzz"]
Example 3:

Input: n = 15
Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

"""
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:
                ans.append(str(i))
        return ans
    
#less time
class Solution:
    def fizzBuzz(self, n: int):
        self.n = n
        numbers_list = []

        if self.n < 1 or self.n > 10000:
            raise Exception("Invalid input for n")

        self.create_numbers_list(numbers_list)
        return numbers_list

    def create_numbers_list(self, list):
        i = 1
        while i <= self.n:
            if i % 3 == 0 and i % 5 == 0:
                list.append("FizzBuzz")
            elif i % 3 == 0:
                list.append("Fizz")
            elif i % 5 == 0:
                list.append("Buzz")
            else:
                list.append(str(i))
            i += 1

#less memory
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        return ("Fizz"*(i%3==0) + "Buzz"*(i%5==0) or str(i) for i in range(1,n+1))