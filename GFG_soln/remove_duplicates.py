class Solution:
    def remove_Duplicates(self, arr):
        ans = []
        if(len(arr) == 0):
            return ans
        j = 0
        ans.append(arr[0])
        for i in range(1, len(arr)):
            if arr[i] != arr[j]:
                ans.append(arr[i])
                j = i
        return ans
    

arr = [1,2,5,4,4,4]
obj = Solution()
result = obj.remove_Duplicates(arr)
print(result)
