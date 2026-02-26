class Solution:
    def getAlternate(self, arr):
        n = len(arr)
        res = []
        for i in range(0, n, 2):
            res.append(arr[i])
        return res
    

arr = [2,3,1,4,5]
obj = Solution()
result = obj.getAlternate(arr)
print(result)
