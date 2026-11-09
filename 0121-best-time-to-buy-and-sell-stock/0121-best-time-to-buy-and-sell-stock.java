class Solution {
    public int maxProfit(int[] prices) {
        int maxi=0;
        int curr=prices[0];
        for(int i=1;i<prices.length;i++){
            if(curr>prices[i]){
                curr=prices[i];
                
            }
            maxi=Math.max(prices[i]-curr,maxi);
        }
        return maxi;
    }
}