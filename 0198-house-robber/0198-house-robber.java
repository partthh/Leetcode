class Solution {
    public int rob(int[] nums) {
        if(nums.length==1){
            return nums[0];
        }
        int prev=nums[0];
        int prev2=0;
        // int curr=-1;
        for(int i=1;i<nums.length;i++){
            int pick=nums[i]+prev2;
            int nopick=prev;
            int curr=Math.max(pick,nopick);
            prev2=prev;
            prev=curr;
        }
        return prev;
    }
}