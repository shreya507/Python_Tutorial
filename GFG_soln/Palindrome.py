class Solution:
    def isPalindrome(self, string):
        s = str(string)
        start = 0
        end = len(s) - 1
        while (start<end):
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True
    

# n = 555
string = "aba"
obj = Solution()
result = obj.isPalindrome(string)
print(result)
