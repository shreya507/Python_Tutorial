class Solution:
    def checkString(self, s):
        v = 0 # V will count the vowels
        c = 0 # c will count the consonants
        # Loop through each character of the string
        for i in range(len(s)):
            # check if character is a vowel
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                v += 1 #increase vowel count
                # check if character is a consonant
            elif 'a' <= s[i] <= 'z':
                c += 1 #increase consonant count

        #Compare Counts and print result
        if v > c:
            print("yes") #more vowels than consonants
        elif c > v:
            print("No")  #more consonants than vowels
        else:
            print("Same")  # equal vowels and consonats

        
s = "abcde"

obj = Solution()  #create object of class
obj.checkString(s) # call the function