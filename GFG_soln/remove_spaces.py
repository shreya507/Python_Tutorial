class Solution:
    def remove_spaces(self, s):
        n = len(s)
        res = ""
        for i in range(n):
            if(s[i] != " "):
                res += s[i]
        return res
    

s = "Geeks for geeks"
obj = Solution()
result = obj.remove_spaces(s)
print(result)