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
    public int minimumEffortPath(int[][] heights) {
        PriorityQueue<pair> q1=new PriorityQueue<pair>((a,b)->a.first-b.first);
        int[][] arr=new int[heights.length][heights[0].length];

        int[] dr={0,-1,0,1};
        int[] dc={-1,0,1,0};
        for(int[] arr1:arr){
            Arrays.fill(arr1,Integer.MAX_VALUE);}
        arr[0][0]=0;
        q1.offer(new pair(0,0,0));
        while(!q1.isEmpty()){
            pair n1=q1.poll();
            int first=n1.first;
            int row=n1.row;
            int col=n1.col;
            for(int i=0;i<4;i++){
                int nr=row+dr[i];
                int nc=col+dc[i];
                if(nr>=0 && nc>=0 && nr<heights.length && nc<heights[0].length ){
                    int diff=Math.abs(heights[row][col]-heights[nr][nc]);
                    int maxdiff=Math.max(first,diff);
                    if(arr[nr][nc]>maxdiff){
                        q1.offer(new pair(maxdiff,nr,nc));
                        arr[nr][nc]=maxdiff;
                    }
                }
        }
        }
            return arr[heights.length-1][heights[0].length-1];


    }
}