class Solution {
    public int minimumTotal(List<List<Integer>> triangle) {
        int n=triangle.size();
        int[][] dp=new int[n][triangle.get(n-1).size()];
        for(int[] x:dp){
            Arrays.fill(x,-1);
        }
        for(int i=0;i<n;i++){
            dp[n-1][i]=triangle.get(n-1).get(i);
        }
        for(int i=n-2;i>=0;i--){
            for(int j=0;j<=i;j++){
                int down=dp[i+1][j];
                int rightdown=dp[i+1][j+1];
                dp[i][j]=triangle.get(i).get(j)+Math.min(down,rightdown);
            }
        }
        return dp[0][0];
    }
}