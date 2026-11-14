class Solution {
    public int uniquePaths(int m, int n) {
        int dp[][]=new int[m][n];
        for(int[] x:dp){
            Arrays.fill(x,-1);
        }
        return fun1(m-1,n-1,dp);
    }
    public int fun1(int m,int n,int[][] dp){
        if(m==0 && n==0){
            return 1;
        }
        if(m<0 || n<0){
            return 0;
        }
        if(dp[m][n]!=-1){
            return dp[m][n];
        }
        return dp[m][n]=fun1(m,n-1,dp)+fun1(m-1,n,dp);
    }
}