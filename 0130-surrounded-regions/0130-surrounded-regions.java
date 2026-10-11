class Solution {
    public void dfs(int row,int col,int[][] vis,char[][] board){
        int x=board.length;
        int y=board[0].length;
        vis[row][col]=1;
        int[] dr={0,-1,0,1};
        int[] dc={-1,0,1,0};
        for(int i=0;i<4;i++){
            int nr=row+dr[i];
            int nc=col+dc[i];
            if(nr>0 && nc>0 && nr<x && nc<y && board[nr][nc]=='O' && vis[nr][nc]==0){
                dfs(nr,nc,vis,board);
            }
        }
    }
    public void solve(char[][] board) {
        int x=board.length;
        int y=board[0].length;
        int[][] vis=new int[x][y];
        for(int i=0;i<x;i++){
            for(int j=0;j<y;j++){
                if(i==0 || i==x-1 || j==0 || j==y-1){
                    if(board[i][j]=='O'){
                        dfs(i,j,vis,board);
                    }
                }
            }
        }
        for(int i=0;i<x;i++){
            for(int j=0;j<y;j++){
                if(vis[i][j]==0 && board[i][j]=='O'){
                    board[i][j]='X';
                }
        }
        }
    }
}