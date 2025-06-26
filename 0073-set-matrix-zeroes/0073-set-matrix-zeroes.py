class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        col=len(matrix[0])
        row1=[0]*row
        col1=[0]*col
        
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    row1[i]=-1
                    col1[j]=-1
        for i in range(row):
            for j in range(col):
                if row1[i]==-1:
                    matrix[i][j]=0
                elif(col1[j]==-1):
                    matrix[i][j]=0
        return matrix
        
        
            