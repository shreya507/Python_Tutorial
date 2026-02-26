class Solution:
    def Largest(self, arr):
        temp = arr[0]
        n = len(arr)

        for i in range(0,n):
            temp = max(temp, arr[i])
        
        return temp
    
arr = [2,5,8,92,23]
obj = Solution()
result = obj.Largest(arr)
print(result)