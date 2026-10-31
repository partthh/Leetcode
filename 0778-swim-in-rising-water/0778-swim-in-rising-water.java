class pair{
    int first;
    int row;
    int col;
    pair(int first,int row,int col){
        this.first=first;
        this.row=row;
        this.col=col;
    }
}
    class Solution {
    public int swimInWater(int[][] grid) {
        int n=grid.length;
        int[][] dist=new int[n][n];
        for(int i=0;i<n;i++){
            Arrays.fill(dist[i],Integer.MAX_VALUE);
        }
        dist[0][0]=grid[0][0];

        PriorityQueue<pair> q1=new PriorityQueue<>((a,b)->a.first-b.first);
        q1.offer(new pair(grid[0][0],0,0));
        int[] dr={0,-1,0,1};
        int[] dc={-1,0,1,0};  
        while(!q1.isEmpty()){
            pair p=q1.poll();
            int node=p.first;
            int row=p.row;
            int col=p.col;
            if(row==n-1 && col==n-1)
            {
                    return node;
                }
                if(node>dist[row][col]){
                    continue;
                }
            for(int i=0;i<4;i++){
                int nr=row+dr[i];
                int nc=col+dc[i];
                if(nr>=0 && nc<n && nr<n && nc>=0){
                    int maxt=Math.max(grid[nr][nc],node);
                    if(maxt<dist[nr][nc]){
                        q1.offer(new pair(maxt,nr,nc));
                        dist[nr][nc]=maxt;
                    }
                }
            }
        }
        return -1;  
    }
}