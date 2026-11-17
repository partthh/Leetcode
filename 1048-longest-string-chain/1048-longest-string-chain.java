class Solution {
    public boolean fun1(String word1,String word2){
        if(word2.length()-word1.length()!=1){
            return false;
        }
        int i=0;
        int j=0;
        while(i<word1.length() && j<word2.length()){
            if(word1.charAt(i)==word2.charAt(j)){
                i+=1;
                j+=1;
            }
            else{
                j+=1;
            }
        }
        return i==word1.length();
    }
    public int longestStrChain(String[] words) {
        Arrays.sort(words,(a,b)->a.length()-b.length());
        int[] dp=new int[words.length];
        Arrays.fill(dp,1);
        int maxi=1;
        for(int i=0;i<words.length;i++){
            for(int j=0;j<i;j++){
                if(fun1(words[j],words[i])){
                    dp[i]=Math.max(dp[i],dp[j]+1);
                }
            }
            maxi=Math.max(maxi,dp[i]);
        }
        return maxi;
    }
}