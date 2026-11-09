class Solution {
    public int maxProfit(int[] prices) {
        int profit=0;
        int[][] dp=new int[prices.length+2][2];
        for(int index=prices.length-1;index>=0;index--){
            for(int buy=0;buy<2;buy++){
                if(buy==1){
                    int buying=-prices[index]+dp[index+1][0];
                    int nobuying=0+dp[index+1][1];
                    profit=Math.max(buying,nobuying);
                }
                else{
                    int selling=prices[index]+dp[index+2][1];
                    int noselling=dp[index+1][0];
                    profit=Math.max(selling,noselling);
                }
                dp[index][buy]=profit;
            }
        }
        return dp[0][1];
    }
}