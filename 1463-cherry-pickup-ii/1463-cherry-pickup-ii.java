class Solution {
    public int cherryPickup(int[][] grid) {
        int n=grid.length;
        int[][][] dp=new int[n][grid[0].length][grid[0].length];
        for(int i=0;i<n;i++){
            for(int j=0;j<grid[0].length;j++){
                Arrays.fill(dp[i][j],-1);
            }
        }
        return fun1(0,0,grid[0].length-1,grid,dp);
    }
    public int fun1(int row,int col1,int col2,int[][] grid,int[][][] dp){
        int cherries=0;
        if(col1<0 || col1>=grid[0].length || col2<0 || col2>=grid[0].length){
            return -(int)1e8;
        }
        cherries+=grid[row][col1];
        if(col1!=col2){
            cherries+=grid[row][col2];
        }
        if(row==grid.length-1){
            return cherries;
        }
        if(dp[row][col1][col2]!=-1){
            return dp[row][col1][col2];
        }
        int maxi=Integer.MIN_VALUE;
        for(int i=-1;i<=1;i++){
            for(int j=-1;j<=1;j++){
                maxi=Math.max(maxi,fun1(row+1,col1+i,col2+j,grid,dp));
            }
        }
        return dp[row][col1][col2]=cherries+maxi;
        
    }
}