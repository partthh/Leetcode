class Solution {
    public int fun1(int index,int[] nums,int target,int[][] dp){
        if(index==0){
            if(target==0 && nums[0]==0){
                return 2;
            }
            else if(target==0 || nums[0]==target){
                return 1;
            }
            else{
                return 0;
            }
        }
        if(dp[index][target]!=-1){
            return dp[index][target];
        }
        int pick=0;
        if(nums[index]<=target){
            pick=fun1(index-1,nums,target-nums[index],dp);
        }
        int nopick=fun1(index-1,nums,target,dp);
        return dp[index][target]=pick+nopick;
    }
    public int findTargetSumWays(int[] nums, int target) {
        int sum=0;
        for(int i:nums){
            sum+=i;
        }
        if ((Math.abs(target))>sum){
            return 0;
        }
        int find=sum+target;
        if(find%2!=0){
            return 0;
        }
        find=find/2;
        int[][] dp=new int[nums.length][find+1];
        for(int[] row:dp){
            Arrays.fill(row,-1);
        }
        return fun1(nums.length-1,nums,find,dp);
    }
}