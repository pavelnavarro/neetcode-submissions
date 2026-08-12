class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        currSplit = []

        def dfs(i):
            if i>=len(s):
                res.append(currSplit[:])
                return
                
            for j in range(i,len(s)):
                if self.isPalindrome(s,i,j):
                    currSplit.append(s[i:j+1])
                    dfs(j+1)
                    currSplit.pop()
            

        dfs(0)
        return res

    def isPalindrome(self,word,l,r):
        if not word:
            return True
        while l<=r:
            if word[l]!=word[r]:
                return False
            l+=1
            r-=1
        return True

        