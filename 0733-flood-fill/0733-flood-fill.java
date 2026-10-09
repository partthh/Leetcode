class Solution {
    public int[][] floodFill(int[][] image, int sr, int sc, int color) {
        int[] rdir={0,-1,0,1};
        int[] cdir={-1,0,1,0};
        int[][] ans=image;
        int currcolor=image[sr][sc];
        dfs(sr,sc,ans,image,rdir,cdir,currcolor,color);
        return ans;
    }
    public void dfs(int row,int col,int[][] ans,int[][] image,int[] rdir,int[] cdir,int currcolor,int newcolor){
        ans[row][col]=newcolor;
        int m=image.length;
        int n=image[0].length;
        for(int i=0;i<4;i++){
            int newr=row+rdir[i];
            int newco=col+cdir[i];
            if(newr>=0 && newco>=0 && newr<m && newco<n && ans[newr][newco]==currcolor && ans[newr][newco]!=newcolor){
                dfs(newr,newco,ans,image,rdir,cdir,currcolor,newcolor);
            }
        }
    }
}