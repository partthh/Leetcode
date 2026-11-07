class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n=triangle.size();
        int[][] dp=new int[n][triangle.get(n-1).size()];
        boolean[][] vis=new boolean[n][n];
        for(int[] x:dp){
            Arrays.fill(x,-1);
        }
        return fun1(0,0,triangle,dp,vis);
    }

    public int fun1(int row,int col,List<List<Integer>> triangle,int[][] dp,boolean[][] vis){
        if(row==triangle.size()-1){
            return triangle.get(row).get(col);
        }
        if(vis[row][col]){
            return dp[row][col];
        }
        int down=fun1(row+1,col,triangle,dp,vis);
        int rightdown=fun1(row+1,col+1,triangle,dp,vis);
        dp[row][col]=triangle.get(row).get(col)+Math.min(down,rightdown);
        vis[row][col]=true;
        return dp[row][col];
    }
}