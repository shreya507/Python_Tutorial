class Solution:
    def CountZeros(self, arr):
        n = len(arr)
        count = 0
        for i in range(n):
            if(arr[i] == 0):
                count += 1
        return count
    

arr = [2,0,4,0,0,4,23,0]
obj = Solution()
result = obj.CountZeros(arr)
print(result)