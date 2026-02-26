class Solution:
    def Missing_ele(arr):
        n = len(arr) + 1
        total = (n*(n+1))//2
        sum = 0
        for i in range(len(arr)):
            sum += arr[i]
        return total - sum
    
arr = [1,2,3,5,6]
obj = Solution
result = obj.Missing_ele(arr)
print(result)