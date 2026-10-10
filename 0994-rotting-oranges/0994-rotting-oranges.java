class Pair{
    int first;
    int second;
    public Pair(int first,int second){
        this.first=first;
        this.second=second;
    }
}
class Solution {
    public int orangesRotting(int[][] grid) {
        int x=grid.length;
        int y=grid[0].length;
        int r1=0;
        int c1=0;
        int count=0;
        int fresh=0;
        Queue<Pair> q1=new LinkedList<>();
        for(int i=0;i<x;i++){
            for(int j=0;j<y;j++){
                if(grid[i][j]==2){
                    q1.offer(new Pair(i,j));
                }
                if(grid[i][j]==1){
                    fresh+=1;
                }
            }
        }
        int[] rdir={0,-1,0,1};
        int[] cdir={-1,0,1,0};
        if(fresh==0){
            return 0;
        }
        if(q1.isEmpty()){
            return -1;
        }
        while(!q1.isEmpty()){
            int cusize=q1.size();
            for(int v=0;v<cusize;v++){

            
            int r2=q1.peek().first;
            int c2=q1.peek().second;
            q1.remove();
            for(int i=0;i<4;i++){
                int newr=r2+rdir[i];
                int newc=c2+cdir[i];
                if(newr>=0 && newc>=0 && newr<x && newc<y && grid[newr][newc]==1 ){
                    grid[newr][newc]=2;
                    q1.offer(new Pair(newr,newc));
                }
            }
            }
            count+=1;
        }
         for(int i=0;i<x;i++){
            for(int j=0;j<y;j++){
                if(grid[i][j]==1){
                    return -1;
                }
            }
        }
        return count-1;

    }
}