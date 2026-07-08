class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trustDict = defaultdict(set)
        for person,trusts in trust:
            trustDict[person].add(trusts)
        for i in range(1,n+1):
            if i not in trustDict:
                for j in range(1,n+1):
                    if j == i:
                        continue
                    if i not in trustDict[j]:
                        return -1
                return i
        return -1

        