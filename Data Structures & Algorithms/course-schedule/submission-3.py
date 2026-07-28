class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courseDict = defaultdict(list)
        for course,pre in prerequisites:
            courseDict[course].append(pre)
        
        visited = set()

        def dfs(course):
            if course not in courseDict or not courseDict[course]:
                return True
            if course in visited:
                return False

            visited.add(course)
            for pre in courseDict[course]:
                if not dfs(pre):
                    return False

            courseDict[course]=[]
            return True
                
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True
        

        