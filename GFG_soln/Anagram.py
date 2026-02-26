class Solution:
    def anagram_Check(self, s1, s2):
        if len(s1) != len(s2):
            return False
        
        s1 = sorted(s1)
        s2 = sorted(s2)

        return s1==s2
    

s1 = "geeks"
s2 = "kseeg"
obj = Solution()
res = obj.anagram_Check(s1, s2)
print(res)