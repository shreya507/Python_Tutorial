class Solution:
    def arraySum(self, arr):
        res = 0
        n = len(arr)
        for i in range(n):
            res += arr[i]
        return res
    
arr = [1,4,3,5,6]
obj = Solution()
result = obj.arraySum(arr)
print(result)