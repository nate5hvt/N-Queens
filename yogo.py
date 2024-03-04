def arrange(board):
    a=[]
    for i in board:
        s=""
        for j in i:
            s+=j
        a.append(s)
    return a

def solve(row,board,col,diagonal,antidiagonal,n,ans):
    if(row==n):
        ans.append(arrange(board))
        return
    for i in range(n):
        if((i in col) or ((row-i) in diagonal) or ((row+i) in antidiagonal)):
            continue
        board[row][i]="Q"
        col.add(i)
        diagonal.add(row-i)
        antidiagonal.add(row+i)

        solve(row+1,board,col,diagonal,antidiagonal,n,ans)

        board[row][i]="."
        col.remove(i)
        diagonal.remove(row-i)
        antidiagonal.remove(row+i)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col=set()
        diagonal=set()
        antidiagonal=set()
        board=[["." for i in range(n)] for j in range(n)]
        ans=[]
        solve(0,board,col,diagonal,antidiagonal,n,ans)
        return(ans)