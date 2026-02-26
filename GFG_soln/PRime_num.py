class Solution:
    def Prime_num(self, n):
        if(n<=1):
            return False
        for i in range(2, n):
            if(n%i == 0):
                return False
        return True
    

n = 11
obj = Solution()
result = obj.Prime_num(n)
print(result)