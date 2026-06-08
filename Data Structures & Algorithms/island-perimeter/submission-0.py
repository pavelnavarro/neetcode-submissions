class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows,cols = len(grid),len(grid[0])
        visited = set()
        res = 0
        def dfs(r,c):
            nonlocal res
            if (r,c) in visited or r not in range(rows) or c not in range(cols):
                return
            if grid[r][c]==1:
                sides = 4
                moves = [(1,0),(-1,0),(0,1),(0,-1)]
                for mr,mc in moves:
                    nr,nc = r+mr,c+mc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc]==1:
                        sides-=1
                res+=sides
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)
        dfs(0,0)
        return res
            
            
                

        