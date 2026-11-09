class Solution {
    public int fun1(int index,int buy,int[] prices,int n,int[][] dp){
        int profit=0;
        
        if(index>=n){
            return 0;
        }
        if(dp[index][buy]!=-1){
            return dp[index][buy];
        }
        if(buy==1){
            int pick=-prices[index]+fun1(index+1,0,prices,n,dp);
            int nopick=0+fun1(index+1,1,prices,n,dp);
            profit=Math.max(pick,nopick);
        }
        else{
            int pick=prices[index]+fun1(index+2,1,prices,n,dp);
            int nopick=fun1(index+1,0,prices,n,dp);
            profit=Math.max(pick,nopick);
        }
        return dp[index][buy]=profit;
        
    }
    public int maxProfit(int[] prices) {
        int[][] dp=new int[prices.length][2];
        for(int[] i:dp){
            Arrays.fill(i,-1);
        }
        return fun1(0,1,prices,prices.length,dp);
    }
}