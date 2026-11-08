//bottom up 
class Solution {
    public int cherryPickup(int[][] grid) {
        int n=grid.length;
        int m=grid[0].length;
        int[][][] dp=new int[n][grid[0].length][grid[0].length];
        //base case 
        for(int i=0;i<m;i++){
            for(int j=0;j<m;j++){
                if(i==j){
                    dp[n-1][i][j]=grid[n-1][i];
                }
                else{
                    dp[n-1][i][j]=grid[n-1][i]+grid[n-1][j];
                }
            }
        }


        for(int row=n-2;row>=0;row--){
            for(int col1=0;col1<m;col1++){
                for(int col2=0;col2<m;col2++){
                    int maxi=Integer.MIN_VALUE;
                    for(int i=-1;i<=1;i++){
                        for(int j=-1;j<=1;j++){
                            int ncol1=col1+i;
                            int ncol2=col2+j;
                            if(ncol1>=0 && ncol2>=0 && ncol1<m && ncol2<m){
                                maxi=Math.max(maxi,dp[row+1][col1+i][col2+j]);
                            }
                        }
                    }
                    if(col1==col2){
                        dp[row][col1][col2]=grid[row][col1]+maxi;
                    }
                    else{
                        dp[row][col1][col2]=grid[row][col1]+grid[row][col2]+maxi;
                    }
                }
            }
        }
        return dp[0][0][m-1];
    }
        
    }
    