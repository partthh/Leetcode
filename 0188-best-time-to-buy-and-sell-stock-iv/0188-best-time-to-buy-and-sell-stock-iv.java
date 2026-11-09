class Solution {
    public int fun1(int index,int canbuy,int cap,int[] prices,int[][][] dp){
        int profit=0;
        if(cap==0){
            return 0;
        }
        if(index==prices.length){
            return 0;
        }
        if(dp[index][canbuy][cap]!=-1){
            return dp[index][canbuy][cap];
        }
        if(canbuy==1){
            int buying=-prices[index]+fun1(index+1,0,cap,prices,dp);
            int nobuying=fun1(index+1,1,cap,prices,dp);
            profit=Math.max(buying,nobuying);
        }
        else{
            int sell=prices[index]+fun1(index+1,1,cap-1,prices,dp);
            int nosell=fun1(index+1,0,cap,prices,dp);
            profit=Math.max(sell,nosell);
        }
        return dp[index][canbuy][cap]=profit;
        
    }
    public int maxProfit(int k, int[] prices) {
        int[][][] dp=new int[prices.length][2][k+1];
        for(int[][] matrix:dp){
            for(int[] row:matrix){
                Arrays.fill(row,-1);
            }
        }
        return fun1(0,1,k,prices,dp);
    }
}