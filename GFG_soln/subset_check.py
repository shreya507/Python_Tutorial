class Solution:
    def solve(self, ans, output, i, nums):
        # base case
        if i >= len(nums):
            ans.append(output.copy())   # important: copy list
            return
        
        # include current element
        output.append(nums[i])
        self.solve(ans, output, i + 1, nums)
        
        # backtrack and exclude current element
        output.pop()
        self.solve(ans, output, i + 1, nums)
    
    def subsets(self, arr):
        # code here
        arr.sort()
        
        ans = []
        output = []
        
        self.solve(ans, output, 0, arr)
        
        ans.sort()
        return ans
        

arr = [1,2,5]
obj = Solution()
result = obj.subsets(arr)
print(result)