class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        currWord = []
        visited = set()
        rows,cols = len(board),len(board[0])
        directions = [(0,1),(0,-1),(1,0),(-1,0)]

        #return True if word exists
        def dfs(r,c):
            if (
                r not in range(rows)
                or c not in range(cols)
                or (r, c) in visited
                or board[r][c] != word[len(currWord)]
            ):
                return False
            
            currWord.append(board[r][c])
            visited.add((r,c))
            if len(currWord) == len(word):
                return True
                
            for mr,mc in directions:
                nr,nc = r+mr,c+mc
                if dfs(nr,nc):
                    return True
            currWord.pop()
            visited.remove((r,c))
            return False
        
        for r in range(rows):
            for c in range(cols):
                if board[r][c]==word[0]:
                    if dfs(r,c):
                        return True
        return False

        