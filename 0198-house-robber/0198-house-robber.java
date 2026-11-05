class Solution {
    public int rob(int[] nums) {
        int[] dp=new int[nums.length];
        Arrays.fill(dp,-1);
        return fun1(nums.length-1,nums,dp);
    }
    public int fun1(int x,int[] nums,int[] dp){
        if(x<0){
            return 0;
        }
        if(x==0){
            return nums[0];
        }
        if(dp[x]!=-1){
            return dp[x];
        }
        int pick=fun1(x-2,nums,dp)+nums[x];
        int nopick=fun1(x-1,nums,dp);
        return dp[x]=Math.max(pick,nopick);
    }
}