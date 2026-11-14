class Solution {
    public int fun1(int index,int prev,int[] nums,int[][] dp){
        if(index==nums.length){
            return 0;
        }
        if(dp[index][prev+1]!=-1){
            return dp[index][prev+1];
        }
        int nopick=fun1(index+1,prev,nums,dp);
        int pick=0;
        if(prev==-1 || nums[index]>nums[prev]){
            pick=1+fun1(index+1,index,nums,dp);
        }
        return dp[index][prev+1]=Math.max(pick,nopick);
    }
    public int lengthOfLIS(int[] nums) {
        int[][] dp=new int[nums.length][nums.length+1];
        for(int[] row:dp){
            Arrays.fill(row,-1);
        }
        return fun1(0,-1,nums,dp);
    }
}