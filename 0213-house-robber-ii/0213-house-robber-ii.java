class Solution {
    public int rob(int[] nums) {
        if(nums.length==1){
            return nums[0];
        }
        int[] arr1=new int[nums.length];
        int[] arr2=new int[nums.length];
        for(int i=0;i<nums.length;i++){
            arr1[i]=nums[i];
            arr2[i]=nums[i];
        }
        arr1[nums.length-1]=0;
        arr2[0]=0;
        return Math.max(fun1(nums.length-1,arr1),fun1(nums.length-1,arr2));
    }
    public int fun1(int x,int[] nums1){
        int prev=nums1[0];
        int prev1=0;
        for(int i=1;i<nums1.length;i++){
            int pick=nums1[i]+prev1;
            int nopick=prev;
            int curr=Math.max(pick,nopick);
            prev1=prev;
            prev=curr;
        }
        return prev;
    }
}