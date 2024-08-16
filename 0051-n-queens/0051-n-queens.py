class Solution(object):
    def __init__(self):
        
        self.result=[]
    def valid(self,board,row,col):
        for i in range(row):
            if(board[i][col]=="Q"):
                return False
        i=row
        j=col
        while(i>=0 and j>=0):
            if(board[i][j]=="Q"):
                return False
            i-=1
            j-=1
        i=row
        j=col
        while(i>=0 and j<len(board)):
            if(board[i][j]=='Q'):
                return False
            i-=1
            j+=1
        return True
            

    def solve(self,board,row):
        if row==len(board):
            self.result.append(["".join(r) for r in board])
            return
        for i in range(len(board)):
            if self.valid(board,row,i):
                board[row][i]="Q"
                self.solve(board,row+1)
                board[row][i]="."


    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        if n==0:
            return []
        self.result=[]
        board=[]
        for i in range(n):
            row=[]
            for j in range(n):
                row.append('.')
            board.append(row)
        self.solve(board,0)
        return self.result