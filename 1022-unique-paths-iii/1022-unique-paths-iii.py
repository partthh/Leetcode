class Solution(object):
    def __init__(self):
        self.direction=[(0,-1),(0,1),(-1,0),(1,0)]
        self.result=0
    def solve(self,grid,i,j,current):
        
        if(i<0 or j<0 or i>=self.row or j>=self.col or grid[i][j]==-1):
            return 
        if(grid[i][j]==2 ):
            if(current==self.empty):
                self.result+=1
            return
        
        grid[i][j]=-1
        for x1,x2 in self.direction:
            newx1=i+x1
            newx2=j+x2
            
            self.solve(grid,newx1,newx2,current+1)
        grid[i][j]=0
        
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.col=len(grid[0])
        self.row=len(grid)
        self.empty=1
        start_row, start_col = 0, 0

        # count=0
        self.result=0
        for i in range(self.row):
            for j in range(self.col):
                if(grid[i][j]==0):
                    self.empty+=1
                elif(grid[i][j]==1):
                    start_row, start_col = i, j
        self.solve(grid,start_row, start_col,0)
        return self.result
            