class Solution {
    public void reverse(int[] nums,int start, int end){
        while(start<end){
            int temp1=nums[start];
            nums[start]=nums[end];
            nums[end]=temp1;
            start+=1;
            end-=1;
        }
    }
    public void rotate(int[] nums, int k) {
        k=k%nums.length;
        reverse(nums,0,nums.length-1);
        reverse(nums,0,k-1);
        reverse(nums,k,nums.length-1);
    }
}