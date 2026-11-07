class Solution {
    public int uniquePathsWithObstacles(int[][] obstacleGrid) {
        int m=obstacleGrid.length;
        int n=obstacleGrid[0].length;
        int[][] dp=new int[m][n];
        for(int[] i:dp){
            Arrays.fill(i,-1);
        }
        for(int i=0;i<m;i++){
            for(int j=0;j<n;j++){
                if(obstacleGrid[i][j]==1){
                    dp[i][j]=-2;
                }
            }
        }
        return fun1(m-1,n-1,obstacleGrid,dp);
    }
    public int fun1(int row,int col,int[][] obstacleGrid,int[][] dp){
        if(row<0 || col<0){
            return 0;
        }
        if(dp[row][col]==-2){
            return 0;
        }
        if(row==0 && col==0){
            return 1;
        }
        
        if(dp[row][col]!=-1){
            return dp[row][col];
        }
        int left=0;
        int up=0;
        left=fun1(row,col-1,obstacleGrid,dp);
        up=fun1(row-1,col,obstacleGrid,dp);
        
        return dp[row][col]=left+up;
    }
}