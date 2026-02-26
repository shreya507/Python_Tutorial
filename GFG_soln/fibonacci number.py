class Solution:
    def fib(self, n):
        a = 0
        b = 1
        c = 0
        if n== 0:
            return a
        elif n == 1:
            return b
        else:
            for i in range(2, n+1):
                c = a+b
                a = b
                b = c
            return c
        
n = 15
obj = Solution()
res = obj.fib(n)
print(res)