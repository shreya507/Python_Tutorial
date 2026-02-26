# Dict is mutable, unordered, indexed and cannot contaain duplicate keys
# d = {} #Empty Dictionary
marks = {
    "Harry":90, 
    "Shruthi": 98,
    "Shivansh":89,
    "Shivika":78,
    0:"Sakshi"
}
# print(marks, type(marks))
print(marks["Shruthi"])

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Harry": 67, "Renuka":85})
print(marks)
print(marks.get("Shruthi"))
print(marks["Shruthi"])
# print(marks.get("Shruth1")) #prints None
# print(marks["Shruthi1"])  #return as key error

value = marks.pop('Harry')
print(value)
print(marks)

item = marks.popitem()
print(item)
print(marks)
