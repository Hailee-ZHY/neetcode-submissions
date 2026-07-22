class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l = len(num2)
        i = 0 
        res = 0
        
        while l > 0:
            res += int(num2[l-1]) * self.helper(10, i) * int(num1)
            l  -= 1 
            i +=1 
        return str(res)

    def helper(self, x, n):
        if x == 0:
            return 0

        if n == 0:
            return 1
        else:
            return x * self.helper(x, n-1)

        
