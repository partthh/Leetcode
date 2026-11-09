class Solution {
    public int fun1(int index,int buy,int cap,int[] prices,int[][][] dp){
        int profit=0;
        if(cap==0){
            return 0;
        }
        if(index==prices.length){
            return 0;
        }
        if(dp[index][buy][cap]!=-1){
            return dp[index][buy][cap];
        }
        if(buy==1){
            int canbuy=-prices[index]+fun1(index+1,0,cap,prices,dp);
            int nobuy=fun1(index+1,1,cap,prices,dp);
            profit=Math.max(canbuy,nobuy);
        }
        else{
            int sell=prices[index]+fun1(index+1,1,cap-1,prices,dp);
            int nosell=fun1(index+1,0,cap,prices,dp);
            profit=Math.max(sell,nosell);
        }
        return dp[index][buy][cap]=profit;
    }
    public int maxProfit(int[] prices) {
        int[][][] dp=new int[prices.length][2][3];
        for(int i=0;i<prices.length;i++){
            for(int j=0;j<2;j++){
                Arrays.fill(dp[i][j],-1);
            }
            
        }
        return fun1(0,1,2,prices,dp);
    }
}