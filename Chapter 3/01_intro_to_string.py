a = 'shruthi' #Single quoted string
b = "Shruthi" #Double quoted string
c = '''Shruthi''' #Triple quoted string

# Slicing (negative or positive)
name = "Harry"
print(name[0:3])
print(name[-4:-1])
print(name[:4]) #is same as print(name[0:4])
print(name[1:]) #is same as print(name[1:5])
print(name[1:5])
# nameshort = len(name)
nameshort = name[0:3] #start from index 0 all the way till 3(excluding 3)
print(nameshort)
character1 = name[1]
print(character1)

word1 = "abcdefghijklmnopqrstuvwxyz"
print(word1[1:6:2])


# Length 
word2 = "Wonderful anna"
print(len(word2))
print(word2.endswith("ful"))
print(word2.startswith("Won"))
print(name.capitalize())
print(word2.upper())
print(word2.lower())
# print(Count(word2))
print(word2.find("der"))
print(word2.replace("anna", "PYTHON"))
print(word2.split())