class Solution(object):
    
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        
        row=len(matrix)
        col=len(matrix[0])
        set1=set()
        set2=set()
        for i in range(row):
            for j in range(col):
                if matrix[i][j]==0:
                    set1.add(i)
                    set2.add(j)
        for j in set1:
            for i in range(col):
                matrix[j][i]=0
        for j in set2:
            for i in range(row):
            # for j in set2:
                matrix[i][j]=0
        return matrix
                    