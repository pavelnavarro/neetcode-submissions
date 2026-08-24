class Solution:
    def tribonacci(self, n: int) -> int:
        if n==0:
            return 0
        if n==1:
            return 1
        if n==2:
            return 1

        num0,num1,num2 = 0,1,1
        
        for i in range(n-2):
            temp1 = num1
            temp2= num2
            num2 = num0+num1+num2
            num1 = temp2
            num0 = temp1

        return num2

        