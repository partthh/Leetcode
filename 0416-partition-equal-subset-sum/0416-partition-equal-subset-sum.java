class Solution {
    public boolean fun1(int index,int target,Boolean[][] dp,int[] nums){
        if(target==0){
            return true;
        }
        if(index==0){
            return false;
        }
        if(dp[index][target]!=null){
            return dp[index][target];
        }
        Boolean pick=false;
        if(nums[index]<=target){
            pick=fun1(index-1,target-nums[index],dp,nums);
        }
        Boolean nopick=fun1(index-1,target,dp,nums);
        return dp[index][target]=pick || nopick;
    }
    public boolean canPartition(int[] nums) {
        int target=0;
        for(int i=0;i<nums.length;i++){
            target+=nums[i];
        }
        if (target%2!=0){
            return false;
        }
        target=target/2;
        Boolean[][] dp=new Boolean[nums.length][target+1];
        return fun1(nums.length-1,target,dp,nums);
    }
}