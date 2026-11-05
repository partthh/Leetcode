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
        if(x<0){
            return 0;
        }
        if(x==0){
            return newa[0];
        }
        if(dp[x]!=-1){
            return dp[x];
        }
        int pick=newa[x]+fun1(x-2,dp,newa);
        int nopick=fun1(x-1,dp,newa);
        return dp[x]=Math.max(pick,nopick);
    }
}