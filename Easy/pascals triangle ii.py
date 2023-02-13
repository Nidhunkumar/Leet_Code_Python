'''Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: rowIndex = 3
Output: [1,3,3,1]
Example 2:

Input: rowIndex = 0
Output: [1]
Example 3:

Input: rowIndex = 1
Output: [1,1]'''
numRows=5
#list to store triangle 
triangle = []
#add first row which is always 1
triangle.append([1])

#run for loop for numRows-1 
# for i in range(numRows-1):
#   #list to store row#Initialize with 1 as 1st element is always 1
#   new=[1]#run for loop to add 2 numbers of previous rows
#   for j in range(0,i):
#       print(i,j)
#       new.append(triangle[i][j]+triangle[i][j+1])
#   #add last element of row
#   new.append(1)
#   #add row in a triangle
#   triangle.append(new)
for i in range(5):
    print(i)
    new=[1]
    print(new)
  