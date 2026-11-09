class Solution {
    public int maxProfit(int[] prices) {
        int[][][] dp=new int[prices.length+1][2][3];
        for(int i=prices.length-1;i>=0;i--){
            for(int cap=1;cap<=2;cap++){
                int canbuy=-prices[i]+dp[i+1][0][cap];
                int nobuy=dp[i+1][1][cap];
                dp[i][1][cap]=Math.max(canbuy,nobuy);
                int sell=prices[i]+dp[i+1][1][cap-1];
                int nosell=dp[i+1][0][cap];
                dp[i][0][cap]=Math.max(sell,nosell);
                }
            }
            return dp[0][1][2];
        }
    
    }
