class Pair{
    int first;
    int second;
    public Pair(int first,int second){
        this.first=first;
        this.second=second;
    }
}
class Solution {
    public int numEnclaves(int[][] grid) {
        Queue<Pair> q1=new LinkedList<>();
        int x=grid.length;
        int y=grid[0].length;
        int[][] vis=new int[x][y];
        for(int i=0;i<x;i++){
            for (int j=0;j<y;j++){
                if(i==0 || i==x-1 || j==0 || j==y-1){
                    if(grid[i][j]==1){
                        q1.offer(new Pair(i,j));
                        vis[i][j]=1;
                    }
                }
            }
        }
        int[] delrow={0,-1,0,1};
        int[] delcol={-1,0,1,0};
        while(!q1.isEmpty()){
            int row=q1.peek().first;
            int col=q1.peek().second;
            q1.remove();
            for(int i=0;i<4;i++){
                int nr=row+delrow[i];
                int nc=col+delcol[i];
                if(nr>=0 && nc>=0 && nr<x && nc<y && grid[nr][nc]==1 && vis[nr][nc]==0){
                    q1.add(new Pair(nr,nc));
                    vis[nr][nc]=1;
                }
            }
        }
        int ans=0;
        for(int i=0;i<x;i++){
            for(int j=0;j<y;j++){
                if(vis[i][j]==0 && grid[i][j]==1){
                    ans+=1;
                }
            }
        }
        return ans;
    }
}