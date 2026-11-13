class Solution {
    public int coinChange(int[] coins, int amount) {
        int max_value=(int)1e9;
        int[][] dp=new int[coins.length+1][amount+1];
        for(int [] row:dp){
            Arrays.fill(row,-1);
        }
        for(int target=0;target<=amount;target++){
            if(target%coins[0]==0){
                dp[0][target]=target/coins[0];
            }
            else{
                dp[0][target]=max_value;
            }
        }
        for(int index=1;index<coins.length;index++){
            for(int target=0;target<=amount;target++){
                int pick=max_value;
                if(coins[index]<=target){
                    pick=1+dp[index][target-coins[index]];
                }
                int nopick=dp[index-1][target];

                dp[index][target]=Math.min(pick,nopick);
            }
        }
        int ans= dp[coins.length-1][amount];
        if(ans<max_value){
            return ans;
        }
        return -1;
    }
}