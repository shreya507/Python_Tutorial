# Print the greatest function
# def greatest(a, b, c):
#     if(a>b and a>c):
#         return a
#     elif(b>a and b>c):
#         return b
#     elif(c>a and c>b):
#         return c

# a =34
# b = 78
# c = 67
# print(greatest(a,b,c))



# Celsius to farenheit
def  farein_to_cels(f):
    return 5*(f-32)/9

f = int(input("Enter temperature in F: "))
c = farein_to_cels(f)
print(f"{round(c, 2)} degree to Celsius ")



# How do you prevent a python print() function to print a new line at the end
print("a")
print("b")
print("c", end="")
print("a", end="")



# Converts inch into CM
def inch_to_cm(inch):
      return inch * 2.54

n = int(input("Enter value in inches: "))
print(f"The corresponding value in cms is {inch_to_cm(n)}")



# Remove the string in list
def rem(l, word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
        return n
        # l.remove(word)
        # return l
    
l = ["Shruti", "shr", "an", "ant"]
print(rem(l, "an"))


def mult(n):
    for i in range(1, n+1):
        print(f"{n} X {i} = {n*i}")

mult(5)