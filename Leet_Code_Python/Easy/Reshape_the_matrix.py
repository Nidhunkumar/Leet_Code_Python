'''
566. Reshape the Matrix

In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.


Example 1:


Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]
Example 2:


Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]


'''
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c != len(mat)* len(mat[0]):
            return mat

        final = []
        temp = 0
        c_temp = 0
        row = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if c_temp == c:
                    final.append(list(row))
                    row.clear()
                    c_temp = 0

                row.append(mat[i][j])
                c_temp += 1
        if row:
            final.append(list(row))
        return final
        
#less time

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        mat_flatten = list(chain(*mat))
        if len(mat_flatten) / c != r:
            return mat
        result = []
        for i in range(0, len(mat_flatten), c):
            result.append(mat_flatten[i: i + c])
        return result
    
#less memory

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r*c!=len(mat)*len(mat[0]):
            return mat
        ans=[[]]
        
        d1=len(mat)
        d2=len(mat[0])
        i1=0
        for i in range(d1):
            for j in range(d2):
                ans[-1].append(mat[i][j])
                i1+=1
                if i1==c:
                    ans.append([])
                    i1=0
        if ans[-1]==[]:
            ans.pop()
        return ans