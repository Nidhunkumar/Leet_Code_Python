'''
463. Island Perimeter

You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island. One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4


'''

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        per=0
        def walaco(i,j,grid):
            w=0
            r=len(grid)
            c=len(grid[0])
            if j==0 or grid[i][j-1]==0 :
                w+=1  
            if i==0 or grid[i-1][j]==0:
                w+=1
            if i==r-1 or grid[i+1][j]==0 :
                w+=1
            if j==c-1 or grid[i][j+1]==0:
                w+=1
            return w
        for i in range(r):
            for j in range(c):
                if grid[i][j]==1:
                    per+=walaco(i,j,grid)
        return per

        

#less time
class Solution:

    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        result = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    result += 4
                    if r > 0 and grid[r- 1][c] == 1:
                        result -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        result -= 2
        return result
        
#less memory
DIRECTIONS = ((-1, 0), (1, 0), (0, -1), (0, 1))

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        perimeter = sum(sum(line) for line in grid) * 4
        
        for y in range(n):
            for x in range(m):
                for dy, dx in DIRECTIONS:
                    if not (0 <= y + dy < n and 0 <= x + dx < m):
                        continue
                    if grid[y][x] and grid[y + dy][x + dx]:
                        perimeter -= 1
        
        return perimeter

