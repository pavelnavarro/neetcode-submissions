class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights),len(heights[0])
        pacificSet = set()
        atlanticSet = set()
        res = []
        
        directions= [(0,1),(0,-1),(1,0),(-1,0)]
        #fill the sets
        def dfs(r,c,sea):
            if (r,c) in sea:
                return
            sea.add((r,c))
            for mr,mc in directions:
                nr,nc = r+mr,c+mc
                if nr in range(rows) and nc in range(cols) and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc,sea)
            
        #run the dfs on the pacific
        for i in range(cols):
            dfs(0,i,pacificSet)
        for i in range(rows):
            dfs(i,0,pacificSet)

        #run the dfs on the atlantic
        for i in range(cols):
            dfs(rows-1,i,atlanticSet)
        for i in range(rows):
            dfs(i,cols-1,atlanticSet)

        for cell in pacificSet:
            if cell in atlanticSet:
                res.append([cell[0],cell[1]])
        
        return res

        