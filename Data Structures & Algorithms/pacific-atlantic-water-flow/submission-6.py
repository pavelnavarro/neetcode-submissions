class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights),len(heights[0])
        res = []
        pacific = []
        atlantic = []
        visited = set()
        
        #explore the cells
        def dfs(val,r,c,visits):
            if (r,c) in visited or r not in range(rows) or c not in range(cols) or heights[r][c]<val:
                return
            visits.append([r,c])
            visited.add((r,c))

            val = heights[r][c]

            dfs(val,r+1,c,visits)
            dfs(val,r-1,c,visits)
            dfs(val,r,c+1,visits)
            dfs(val,r,c-1,visits)
            return

        #call dfs on pacific
        visited = set()
        for i in range(len(heights[0])):
            dfs(0,0,i,pacific)
        for i in range(len(heights)):
            dfs(0,i,0,pacific)

        #call dfs on atlantic
        visited = set()
        for i in range(len(heights[0])):
            dfs(0,len(heights)-1,i,atlantic)
        for i in range(len(heights)):
            dfs(0,i,len(heights[i])-1,atlantic)
        
        for coor in pacific:
            if coor in atlantic:
                res.append(coor)
        return res

        


        