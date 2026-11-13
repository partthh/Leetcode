class Solution {
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
        int[][] dp=new int[nums.length+1][find+1];
        for(int target1=0;target1<=find;target1++){
            if(target1==0 && nums[0]==0){
                
                    dp[0][target1]=2;
                
            }
            else if(target1==0 || nums[0]==target1){
                dp[0][target1]=1;
            }
            else{
                dp[0][target1]=0;
            }
        }
        for(int index=1;index<nums.length;index++){
            for(int target1=0;target1<=find;target1++){
                int pick=0;
                if(nums[index]<=target1){
                    pick=dp[index-1][target1-nums[index]];
                }
                int nopick=dp[index-1][target1];
                dp[index][target1]=pick+nopick;
            }
        }
        return dp[nums.length-1][find];
    }
}