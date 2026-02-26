#Strings are immutable which means that you cannot change them by running function on them
name = input("Enter your name: ")
print(f"Good Afternoon, {name} ")


letter = '''Dear <|Name|>,
You are selected!
<|Date|>'''
print(letter.replace("<|Name|>", "Shruthi").replace("<|Date|", "13 september 2025"))


word1 = "Shruthi is a good girl and shruthi  "
print(name.find("  "))

print(name.replace(" ", " "))


word2 = "Dear shruthi, \nthis python course is nice. \nThanks!"
print(word2)