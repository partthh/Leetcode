class Solution {
    public int fun1(int index,int canbuy,int[] prices,int fee,int[][] dp){
        int profit=0;
        if(index==prices.length){
            return 0;
        }
        if(dp[index][canbuy]!=-1){
            return dp[index][canbuy];
        }
        if(canbuy==1){
            int buying=-prices[index]+fun1(index+1,0,prices,fee,dp);
            int nobuying=fun1(index+1,1,prices,fee,dp);
            profit=Math.max(buying,nobuying);
        }
        else{
            int sell=prices[index]+fun1(index+1,1,prices,fee,dp)-fee;
            int nosell=fun1(index+1,0,prices,fee,dp);
            profit=Math.max(sell,nosell);
        }
        return dp[index][canbuy]=profit;
    }
    public int maxProfit(int[] prices, int fee) {
        int[][] dp=new int[prices.length][2];
        for(int[] x:dp){
            Arrays.fill(x,-1);
        }
        return fun1(0,1,prices,fee,dp);
    }
}