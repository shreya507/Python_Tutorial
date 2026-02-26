# print the average of function 


# Function logic

# def avg():
#     a = int(input("Enter number1: "))
#     b = int(input("Enter number2: "))
#     c = int(input("Enter number3: "))
#     d = int(input("Enter number4: "))

#     average = (a+b+c+d)/4
#     print(average)


# # function call
# avg()
# # avg()
# # avg()




# FUNCTIONS WITH ARGUEMENTS OR PARAMETERS
# def good(name):
#     print("Good Day" + name)
# good("Shruti", "Thanks")



# FUNCTION WITH RETURN VALUE
# def good(name, ending):
#     print("Good Day" + name)
#     print(ending)
#     return "done"


# a = good("Shruti", "Thanks")
# print(a)



# Default parameter
def good(name, ending="Thanks"):
    print(f"Good Day, {name}")
    print(ending)

good("Harry")
