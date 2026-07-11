class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        
        queue = deque()
        fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    fresh+=1
                elif grid[i][j]==2:
                    queue.append((i,j))

        time = 0
        movements = [(0,1),(0,-1),(-1,0),(1,0)]
        while queue:
            if fresh == 0:
                return time
            for _ in range(len(queue)):
                row,col = queue.popleft()
                for mr,mc in movements:
                    nr,nc = row+mr,col+mc
                    if nr in range(rows) and nc in range(cols) and grid[nr][nc]==1:
                        queue.append((nr,nc))
                        grid[nr][nc]=2
                        fresh-=1
            time+=1

        return time if fresh==0 else -1


        