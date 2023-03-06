'''Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]

'''
 def generate(self, numRows: int) -> List[List[int]]:
        
        #list to store triangle 
        triangle = []
        #add first row which is always 1
        triangle.append([1])
         
        #run for loop for numRows-1
        for i in range(numRows-1):
            #list to store row#Initialize with 1 as 1st element is always 1
            new=[1]#run for loop to add 2 numbers of previous rows
            for j in range(0,i):
                new.append(triangle[i][j]+triangle[i][j+1])
            #add last element of row
            new.append(1)
            #add row in a triangle
            triangle.append(new)
            
        return triangle
#less time
 def generate(self, numRows: int) -> List[List[int]]:
        a = [[1]]
        for i in range(1,numRows):
            numls = [x+y for x,y in zip([0]+a[i-1],a[i-1]+[0])]
            a.append(numls)
        return a