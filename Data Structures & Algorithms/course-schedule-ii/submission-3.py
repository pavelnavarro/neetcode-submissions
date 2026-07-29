class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courseDic = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            courseDic[course].append(pre)
        res = []
        cycle = set()
        visited = set()

        def dfs(course):
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)

            for pre in courseDic[course]:
                if not dfs(pre):
                    return False
            

            
            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True
            

        for course in range(numCourses):
            if not dfs(course):
                return []
        return res
        