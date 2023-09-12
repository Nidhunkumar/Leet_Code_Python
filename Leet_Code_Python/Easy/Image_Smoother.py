'''
661. Image Smoother

An image smoother is a filter of the size 3 x 3 that can be applied to each cell of an image by 
rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the blue smoother).
If one or more of the surrounding cells of a cell is not present, we do not consider it in the average (i.e., the average of the four cells in the red smoother).
Given an m x n integer matrix img representing the grayscale of an image, return the image after applying the smoother on each cell of it.
Example 1:


Input: img = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[0,0,0],[0,0,0],[0,0,0]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor(3/4) = floor(0.75) = 0
For the points (0,1), (1,0), (1,2), (2,1): floor(5/6) = floor(0.83333333) = 0
For the point (1,1): floor(8/9) = floor(0.88888889) = 0
Example 2:


Input: img = [[100,200,100],[200,50,200],[100,200,100]]
Output: [[137,141,137],[141,138,141],[137,141,137]]
Explanation:
For the points (0,0), (0,2), (2,0), (2,2): floor((100+200+200+50)/4) = floor(137.5) = 137
For the points (0,1), (1,0), (1,2), (2,1): floor((200+200+50+200+100+100)/6) = floor(141.666667) = 141
For the point (1,1): floor((50+200+200+200+200+100+100+100+100)/9) = floor(138.888889) = 138
'''

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        # dimensions of original image
        m, n = len(img), len(img[0])
        # initialize output matrix with zeros
        res = [[0] * n for _ in range(m)]
        # iterate through each cell in the image
        for i in range(m):
            for j in range(n):
                # calculate the sum of the cells in the 3x3 neighborhood
                total = 0
                count = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        # check if the cell is inside the image
                        if 0 <= x < m and 0 <= y < n:
                            total += img[x][y]
                            count += 1
                # calculate the smoothed value for the cell
                res[i][j] = total // count
        return res
    
#less time 
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        row = len(img)
        colm = len(img[0])
        if row == 1 and colm == 1:
            return img 
        ans = [[]]
        if row == 1:
            img = img[0]
            ans[0].append((img[0]+img[1])//2)
            for i in range(1,colm-1):
                ans[0].append((img[i-1]+img[i]+img[i+1])//3)
            ans[0].append((img[-1]+img[-2])//2)
        elif colm == 1:
            ans[0].append((img[0][0]+img[1][0])//2)
            ans.append([])
            for i in range(1,row-1):  
                ans[-1].append((img[i-1][0]+img[i][0]+img[i+1][0])//3)
                ans.append([])
            ans[-1].append((img[-1][0]+img[-2][0])//2)
        elif row == 2 and colm == 2:
            n = (img[0][0]+img[0][1]+img[1][0]+img[1][1])//4
            return([[n,n],[n,n]])
        elif row == 2:
            n = (img[0][0]+img[0][1]+img[1][0]+img[1][1])//4
            ans = [[n],[n]]
            for j in range(1,colm-1):
                n = (img[0][j-1]+img[0][j]+img[0][j+1]+img[1][j-1]+img[1][j]+img[1][j+1])//6
                ans[0].append(n)
                ans[1].append(n)
            n = (img[0][-1]+img[0][-2]+img[1][-1]+img[1][-2])//4
            ans[0].append(n)
            ans[1].append(n)
        elif colm == 2:
            n = (img[0][0]+img[0][1]+img[1][0]+img[1][1])//4
            ans = [[n,n]]
            for j in range(1,row-1):
                n = (img[j-1][0]+img[j][0]+img[j+1][0]+img[j-1][1]+img[j][1]+img[j+1][1])//6
                ans.append([n,n])
            n = (img[-1][0]+img[-2][0]+img[-1][1]+img[-2][1])//4
            ans.append([n,n])
        else:
            n = (img[0][0]+img[0][1]+img[1][0]+img[1][1])//4
            ans = [[n]]
            for j in range(1,colm-1):
                n = (img[0][j-1]+img[0][j]+img[0][j+1]+img[1][j-1]+img[1][j]+img[1][j+1])//6
                ans[0].append(n)
            n = (img[0][-1]+img[0][-2]+img[1][-1]+img[1][-2])//4
            ans[0].append(n)
            for i in range(1,row-1):
                n = (img[i][0]+img[i][1]+img[i+1][0]+img[i+1][1]+img[i-1][0]+img[i-1][1])//6
                ans.append([n])
                for j in range(1,colm-1):
                    n = (img[i][j-1]+img[i][j]+img[i][j+1]+img[i+1][j-1]+img[i+1][j]+img[i+1][j+1]+img[i-1][j-1]+img[i-1][j]+img[i-1][j+1])//9
                    ans[i].append(n)
                n = (img[i][-1]+img[i][-2]+img[i+1][-1]+img[i+1][-2]+img[i-1][-1]+img[i-1][-2])//6
                ans[i].append(n)
            n = (img[-1][0]+img[-1][1]+img[-2][0]+img[-2][1])//4
            ans.append([n])
            for j in range(1,colm-1):
                n = (img[-1][j-1]+img[-1][j]+img[-1][j+1]+img[-2][j-1]+img[-2][j]+img[-2][j+1])//6
                ans[-1].append(n)
            n = (img[-1][-1]+img[-1][-2]+img[-2][-1]+img[-2][-2])//4
            ans[-1].append(n)
        return ans

#less memory
class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        J, I = len(img), len(img[0])
        ans = []
        temp = [-1, 0, 1]
        cnt = I
        for j in range(J):
            for i in range(I):
                curr = n = 0
                if cnt == I: 
                    ans.append([])
                    cnt = 0
                for jx in temp:
                    v = j+jx
                    if v < 0 or v > J-1:
                        continue
                    for ix in temp:
                        h = i+ix
                        if h < 0 or h > I-1:
                            continue
                        curr += img[v][h]
                        n += 1
                ans[-1].append(curr//n)
                cnt += 1
        return ans
