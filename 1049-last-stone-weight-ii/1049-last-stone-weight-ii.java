class Solution {
    public int lastStoneWeightII(int[] stones) {
        int target=0;
        for(int i:stones){
            target+=i;
        }
  
        boolean[][] dp=new boolean[stones.length+1][target+1];
        for(int i=0;i<=stones.length;i++){
            dp[i][0]=true;
        }
        for(int i=stones.length-1;i>=0;i--){
            for(int curr=1;curr<=target;curr++){
                boolean pick=false;
                if(stones[i]<=curr){
                    pick=dp[i+1][curr-stones[i]];
                }
                boolean nopick=dp[i+1][curr];
                dp[i][curr]=pick || nopick;
            }
        }
        int ans=Integer.MAX_VALUE;
        for(int i=0;i<=target/2;i++){
            if(dp[0][i]){
            ans=Math.min(ans,Math.abs(target-2*i));
            }
        }
        return ans;
    }
}