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
        int[] dp=new int[nums.length];
        Arrays.fill(dp,-1);
        int[] dp1=new int[nums.length];
        Arrays.fill(dp1,-1);
        return Math.max(fun1(nums.length-1,dp,arr1),fun1(nums.length-1,dp1,arr2));
    }
    public int fun1(int x,int[] dp,int[] newa){
        dp[0]=newa[0];
        for(int i=1;i<newa.length;i++){
            int pick=newa[i];
            if(i>1){
                pick+=dp[i-2];
            }
            int nopick=dp[i-1];
            dp[i]=Math.max(pick,nopick);
        }
        return dp[newa.length-1];
    }
}