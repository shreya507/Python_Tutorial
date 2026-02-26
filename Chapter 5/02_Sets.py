# Sets are unordered, unindexed, cannot contain duplicate value and there is no way to change items in sets

# s = {1, 5, 32}  Don't use s = {} as it will create an empty dictionary
S = set() #this is the emoty sets
a = {1, 5, 32, 34, 5, 5, 5, "Shruti"}
print(a, type(a))
a.add(45)
print(a, type(a))
a.remove(1)
print(a, type(a))
