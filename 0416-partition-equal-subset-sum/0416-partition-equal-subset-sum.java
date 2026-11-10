class Solution {
    // public boolean fun1(int index,int target,Boolean[][] dp,int[] nums){
    //     if(target==0){
    //         return true;
    //     }
    //     if(index==nums.length){
    //         return false;
    //     }
    //     if(dp[index][target]!=null){
    //         return dp[index][target];
    //     }
    //     Boolean pick=false;
    //     if(nums[index]<=target){
    //         pick=fun1(index+1,target-nums[index],dp,nums);
    //     }
    //     Boolean nopick=fun1(index+1,target,dp,nums);
    //     return dp[index][target]=pick || nopick;
    // }
    public boolean canPartition(int[] nums) {
        int target=0;
        for(int i=0;i<nums.length;i++){
            target+=nums[i];
        }
        if (target%2!=0){
            return false;
        }
        target=target/2;
        boolean[][] dp=new boolean[nums.length+1][target+1];
        for(int i=0;i<nums.length;i++){
            dp[i][0]=true;
        }
        for(int index=nums.length-1;index>=0;index--){
            for(int y=1;y<=target;y++){
                boolean pick=false;
                if(nums[index]<=y){
                    pick=dp[index+1][y-nums[index]];
                }
                boolean nopick=dp[index+1][y];
                dp[index][y]=pick || nopick;
            }
        }
        return dp[0][target];
    }
}