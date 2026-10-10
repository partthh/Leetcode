class Pair{
    int first;
        int second;
    public Pair(int first,int second){
        this.first=first;
        this.second=second;
    }
}
class Solution {
    public int[][] updateMatrix(int[][] mat) {
        int x=mat.length;
        int y=mat[0].length;
        int[][] res=new int[x][y];
        Queue<Pair> q1=new LinkedList<>();
        for(int i=0;i<x;i++){
            for(int j=0;j<y;j++){
                if(mat[i][j]==0){
                    q1.offer(new Pair(i,j));
                }
            }
        }
        while(!q1.isEmpty()){
            int r1=q1.peek().first;
            int c1=q1.peek().second;
            q1.remove();
            int[] dirr={0,-1,0,1};
            int[] dirc={-1,0,1,0};
            for(int i=0;i<4;i++){
                int nr=r1+dirr[i];
                int nc=c1+dirc[i];
                if(nr>=0 && nc>=0 && nr<x && nc<y && mat[nr][nc]==1){
                    res[nr][nc]=res[r1][c1]+1;
                    mat[nr][nc]=0;
                    q1.offer(new Pair(nr,nc));
                }
            }
        }
        return res;
        


    }
}