s1 = {1, 45, 23}
s2 = {34,7, 1,65}
print(s1.union(s2))
print(s1.intersection(s2))
print({7,1}.issubset(s2))
print(s1.issuperset({7,1}))
print(s1.pop())
s1.clear()