class Solution {
    static final int max_value=(int)1e9;
    public int fun1(int index,int amount,int[] coins,int[][] dp){
        if(amount==0){
            return 1;
        }
        if(index==0){
            if(amount%coins[0]==0){
                return 1;
            }
            else{
                return 0;
            }
        }
        if(dp[index][amount]!=-1){
            return dp[index][amount];
        }
        int pick=0;
        if(coins[index]<=amount){
            pick=fun1(index,amount-coins[index],coins,dp);
        }
        int nopick=fun1(index-1,amount,coins,dp);
        return dp[index][amount]=pick+nopick;
    }
    public int change(int amount, int[] coins) {
        int[][] dp=new int[coins.length+1][amount+1];
        for(int[] row:dp){
            Arrays.fill(row,-1);
        }
        for(int amount1=0;amount1<=amount;amount1++){
            if(amount1%coins[0]==0){
                    dp[0][amount1]=1;
                }
            else{
                dp[0][amount1]=0;
            }
        }
        for(int index=1;index<coins.length;index++){
            for(int amount1=0;amount1<=amount;amount1++){
                int pick=0;
                if(coins[index]<=amount1){
                    pick=dp[index][amount1-coins[index]];
                }
                int nopick=dp[index-1][amount1];
                dp[index][amount1]=pick+nopick;
            }
        }
        if(dp[coins.length-1][amount]==-1){
            return 0;
        }
        return dp[coins.length-1][amount];

    }
}