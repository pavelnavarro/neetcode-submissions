class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjacencyList = {i:[] for i in range(n)}

        for start, end in edges:
            adjacencyList[start].append(end)
            adjacencyList[end].append(start)
        
        visited = set()
        count = 0
        #Explore the whole component

        def dfs(node,prev):
            if node in visited:
                return
            visited.add(node)
            for neighbor in adjacencyList[node]:
                if neighbor==prev:
                    continue
                dfs(neighbor,node)
            return

        for i in range(n):
            if i not in visited:
                count+=1
                dfs(i,i)

        return count
        