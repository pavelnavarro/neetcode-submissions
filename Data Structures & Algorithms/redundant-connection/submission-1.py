class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adjacencyList = defaultdict(list)

        #detect the cycle
        def dfs(node,prev,visited):
            if node in visited:
                return True
            visited.add(node)
            for neighbor in adjacencyList[node]:
                if neighbor==prev:
                    continue
                if dfs(neighbor,node,visited):
                    return True
            return False
        
        for start, end in edges:
            adjacencyList[start].append(end)
            adjacencyList[end].append(start)

            if dfs(start,start, set()):
                return [start,end]
        return []

                