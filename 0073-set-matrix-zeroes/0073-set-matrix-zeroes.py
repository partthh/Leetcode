class Solution(object):
    
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        def setrow(row,col,i):
            for j in range(col):
                if matrix[i][j]!=0:
                    matrix[i][j]=-15301
        def setcol(row,col,j):
            for i in range(row):
                if matrix[i][j]!=0:
                    matrix[i][j]=-15301
        row=len(matrix)
        col=len(matrix[0])
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    setrow(row,col,i)
                    setcol(row,col,j)
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==-15301:
                    matrix[i][j]=0
        return matrix
                    