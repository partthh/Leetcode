class Solution {
    public int maxProfit(int[] prices) {
        int[][] dp=new int[prices.length+1][2];
        for(int i=prices.length-1;i>=0;i--){
                int buy=-prices[i]+dp[i+1][0];
                int nobuy=dp[i+1][1];
                dp[i][1]=Math.max(buy,nobuy);
                int sell=prices[i]+dp[i+1][1];
                int nosell=dp[i+1][0];
                dp[i][0]=Math.max(nosell,sell);
                }
        
        return dp[0][1];
    }
}