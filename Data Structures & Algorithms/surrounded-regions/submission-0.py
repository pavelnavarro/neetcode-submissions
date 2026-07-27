class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows,cols = len(board),len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        #explore unsurrounded regions and place marker T
        def dfs(r,c):
            if board[r][c]!="O":
                return

            board[r][c]="T"

            for mr,mc in directions:
                nr,nc = r+mr,c+mc
                if nr in range(rows) and nc in range(cols) and board[nr][nc]=="O":
                    dfs(nr,nc)

        for i in range(rows):
            dfs(i,0)
            dfs(i,cols-1)
        for i in range(cols):
            dfs(0,i)
            dfs(rows-1,i)
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="T":
                    board[r][c]="O"
                elif board[r][c]=="O":
                    board[r][c]="X"
        return 
        


