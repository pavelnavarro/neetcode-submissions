class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            res += self.palindrome(i,i,s)
            res += self.palindrome(i,i+1,s)
        return res

    def palindrome(self,i,j,s):
        count = 0
        while i>=0 and j<len(s) and s[i]==s[j]:
            count+=1
            i-=1
            j+=1
        return count
            


        