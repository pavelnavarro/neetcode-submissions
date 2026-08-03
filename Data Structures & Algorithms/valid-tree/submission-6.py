class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjacencyList = {i:[] for i in range(n)}
        for node,dest in edges:
            adjacencyList[node].append(dest)
            adjacencyList[dest].append(node)
            
        visited = set()

        #return False if cycle is deteced, fill up visited
        def dfs(node,prev):
            if node in visited:
                return False
            visited.add(node)
            for neighbor in adjacencyList[node]:
                if neighbor==prev:
                    continue
                if not dfs(neighbor,node):
                    return False
            return True
        
        if not dfs(0,0):
            return False
        
        return len(visited)==n
        

        