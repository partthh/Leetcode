class pair{
    int first;
    int x;
    int y;
    pair(int first,int x,int y){
        this.first=first;
        this.x=x;
        this.y=y;
    }
}
class Solution {
    public int shortestPathBinaryMatrix(int[][] grid) {
        Queue<pair> q1=new LinkedList<>();
        int[] dr={0,-1,-1,-1,0,1,1,1};
        int[] dc={-1,-1,0,1,1,1,0,-1};
        q1.add(new pair(1,0,0));
        if(grid[grid.length-1][grid[0].length-1]!=0 || grid[0][0]==1){
            return -1;
        }
        grid[0][0]=1;
        while(!q1.isEmpty()){
            pair node=q1.poll();
            int x=node.x;
            int y=node.y;
            int first=node.first;
            if(x==grid.length-1 && y==grid[0].length-1){
                return first;
            }
            for(int i=0;i<8;i++){
                int nx=x+dr[i];
                int ny=y+dc[i];
                if(nx>=0 && ny>=0 && nx<grid.length && ny<grid[0].length && grid[nx][ny]==0){
                    q1.offer(new pair(first+1,nx,ny));
                    grid[nx][ny]=1;
                }
            }
        }
        return -1;
    }
}