class Solution {
    public int maxProfit(int[] prices, int fee) {
        int profit=0;
        int[][] dp=new int[prices.length+1][2];
        for(int index=prices.length-1;index>=0;index--){
            for(int canbuy=0;canbuy<2;canbuy++){
                if(canbuy==1){
                    int buying=-prices[index]+dp[index+1][0];
                    int nobuying=dp[index+1][1];
                    profit=Math.max(buying,nobuying);
                }
                else{
                    int sell=prices[index]+dp[index+1][1]-fee;
                    int nosell=dp[index+1][0];
                    profit=Math.max(sell,nosell);
                }
                dp[index][canbuy]=profit;

            }
        }
        return dp[0][1];
    }
}