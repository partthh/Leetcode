class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int m=matrix.length;
        int n=matrix[0].length;
        int[][] dp=new int[m][n];
        for(int[] x:dp){
            Arrays.fill(x,-1);
        }
        for (int col=0;col<n;col++) {
            dp[0][col]=matrix[0][col];
        }
        int mini=Integer.MAX_VALUE;
        for(int row=1;row<m;row++){
            for(int col=0;col<n;col++){
                int up=dp[row-1][col];
                int leftd=Integer.MAX_VALUE;
                if(col>0){
                    leftd=dp[row-1][col-1];
                }
                int rightd=Integer.MAX_VALUE;
                if(col<n-1){
                    rightd=dp[row-1][col+1];
                }
                dp[row][col]=matrix[row][col]+Math.min(up,Math.min(leftd,rightd));
            }
        }
        int res=dp[m-1][0];
        for(int i=0;i<n;i++){
            res=Math.min(res,dp[m-1][i]);
        } 
        return res;

    }

}