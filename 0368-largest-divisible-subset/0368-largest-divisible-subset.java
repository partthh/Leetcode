class Solution {
    public List<Integer> largestDivisibleSubset(int[] nums) {
        int[] dp=new int[nums.length];
        int[] hash=new int[nums.length];
        Arrays.fill(dp,1);
        for(int i=0;i<nums.length;i++){
            hash[i]=i;
        }
        Arrays.sort(nums);
        int lastindex=0;
        int maxi=1;
        for(int i=0;i<nums.length;i++){
            for(int j=0;j<i;j++){
                if(nums[i]%nums[j]==0 ){
                    if(dp[i]<dp[j]+1){
                        dp[i]=dp[j]+1;
                        hash[i]=j;
                    }
                }
            }
            if(dp[i]>maxi){
                maxi=dp[i];
                lastindex=i;
            }
        }
        List<Integer> res=new ArrayList<>();
        res.add(nums[lastindex]);
        while(lastindex!=hash[lastindex]){
            lastindex=hash[lastindex];
            res.add(nums[lastindex]);
        }
        Collections.reverse(res);
        return res;
    }
}