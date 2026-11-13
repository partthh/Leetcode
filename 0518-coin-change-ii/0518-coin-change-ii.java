class Solution{
    static final int max_value=(int)1e9;
    public int fun1(int index,int[] coins,int amount,int[][] dp){
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
            pick=fun1(index,coins,amount-coins[index],dp);
        }
        int nopick=fun1(index-1,coins,amount,dp);

        return dp[index][amount]=pick+nopick;

    }
    public int change(int amount, int[] coins) {
        int[][] dp=new int[coins.length][amount+1];
        for(int [] row:dp){
            Arrays.fill(row,-1);
        }
        int ans= fun1(coins.length-1,coins,amount,dp);
        return ans;
    }
}
