class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        deadends = set(deadends)
        if "0000" in deadends:
            return -1
        if target == "0000":
            return 0

        queue = deque(["0000"])
        visited = set(["0000"])
        res = 0

        while queue:
            for _ in range(len(queue)):
                combination = queue.popleft()
                if combination == target:
                    return res
                for i in range(4):
                    plusOneCombination = (
                        combination[0:i]
                        + str(((int(combination[i])+1)+10)%10)
                        + combination[i+1:]
                    )
                    minusOneCombination = (
                        combination[0:i]
                        + str(((int(combination[i])-1)+10)%10)
                        + combination[i+1:]
                    )
                    if plusOneCombination not in visited and plusOneCombination not in deadends:
                        queue.append(plusOneCombination)
                        visited.add(plusOneCombination)
                    if minusOneCombination not in visited and minusOneCombination not in deadends:
                        queue.append(minusOneCombination)
                        visited.add(minusOneCombination)

            res+=1
        return -1





        