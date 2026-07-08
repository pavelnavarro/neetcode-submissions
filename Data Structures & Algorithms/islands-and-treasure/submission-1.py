class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        if not grid:
            return

        queue = deque()
        rows, cols= len(grid), len(grid[0])
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==0:
                    queue.append((i,j))
        
        movements = [(1,0),(-1,0),(0,1),(0,-1)]
        #do a bfs
        distance = 1
        while queue:
            for _ in range(len(queue)):
                r,c = queue.popleft()
                for mr,mc in movements:
                    nr,nc = r+mr,c+mc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc]==2147483647:
                        grid[nr][nc] = distance
                        queue.append((nr,nc))
            distance+=1

        return                

        