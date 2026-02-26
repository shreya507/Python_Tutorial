class Solution:
    def reverse_Words(self, s):
        #step 1: Split the string using "." as separator
        # Example: "i.like.this" -> ["i", "like", "this"]
    
        list = s.split(".")
        # Step 2: Reverse the list of words
        # ["i", "like", "this"] -> ["this", "like", "i"]
        list1 = list[::-1]
        # Step 3: Create a new list to store non-empty words
        list2 = []
        # Step 4: Remove empty strings
        for i in list1:
            if i != "":
                list2.append(i)
        # Step 5: Join words with "." again
        # ["this", "like", "i"] -> "this.like.i"
        ans = ".".join(list2)
        # Step 6: Remove leading or trailing dots if present
        return ans.strip(".")
    

s ="i.like.this.program"
obj = Solution()
result = obj.reverse_Words(s)
print(result)