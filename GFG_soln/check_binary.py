class Solution:
    def check_Binary(self, s):
        n = len(s)
        for i in range(n):
            if(s[i] != "1" and s[i] != "0"):
                return False
        return True
    
s = "101"
obj = Solution()
result = obj.check_Binary(s)
print(result)