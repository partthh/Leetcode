class Solution {
    static final int max_value=(int)1e9;
    public int fun1(int index,int[] coins,int amount,int[][] dp){
        if(index==0){
            if(amount%coins[index]==0){
                return amount/coins[index];
            }
            else{
                return max_value;
            }
        }   
        if(dp[index][amount]!=-1){
            return dp[index][amount];
        }
        int pick=max_value;
        if(coins[index]<=amount){
            pick=1+fun1(index,coins,amount-coins[index],dp);
        }
        int nopick=fun1(index-1,coins,amount,dp);

        return dp[index][amount]=Math.min(pick,nopick);

    }
    public int coinChange(int[] coins, int amount) {
        int[][] dp=new int[coins.length][amount+1];
        for(int [] row:dp){
            Arrays.fill(row,-1);
        }
        int ans= fun1(coins.length-1,coins,amount,dp);
        if(ans<max_value){
            return ans;
        }
        return -1;
    }
}