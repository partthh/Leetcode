class Pair{
    int first;
    int second;
    Pair(int first,int second){
        this.first=first;

        this.second=second;
    }
}
class Solution {
    public int numIslands(char[][] grid) {
        int row=grid.length;
        int col=grid[0].length;
        int count=0;
        int[][] vis=new int[row][col];
        int i=0;
        while(i<row){
            int j=0;
            while(j<col){
                if(grid[i][j]=='1' && vis[i][j]==0){
                    count+=1;
                    bfs(i,j,vis,grid);
                    
                }
                j+=1;
            }
            i++;
        }
        return count;
    }
    public void bfs(int row,int col,int[][] vis,char[][] grid){
        Queue<Pair> q1=new LinkedList<Pair>();
        q1.add(new Pair(row,col));
        int x=grid.length;
        int y=grid[0].length;
        vis[row][col]=1;
        while(!q1.isEmpty()){
            int l=q1.peek().first;
            int k=q1.peek().second;
            q1.remove();
            int[] roww={-1,0,1,0};
            int[] colummn={0,1,0,-1};
            for(int l3=0;l3<4;l3++){
                    int r1=l+roww[l3];
                    int c1=k+colummn[l3];
                    if(r1>=0 && c1>=0 && r1<x && c1<y && vis[r1][c1]==0  && grid[r1][c1]=='1'){
                        vis[r1][c1]=1;
                        q1.offer(new Pair(r1,c1));
                    }
                
            }
        }
    }
}