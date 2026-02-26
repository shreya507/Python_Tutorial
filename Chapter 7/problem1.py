#Multiplication table of given number using for loop

# n = int(input("Enter a number: "))
# for i in range(1,5):
#     print(f"{n} X {i} = {n * i}")



#given all the person names starts with 's

# l = ["Harsh", "Soham", "Shruti", "Shubham", "Rahul"]
# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello  {name}")



#find the whether number is prime or not
# n = int(input("Enter a number: "))
# for i in range(2, n):
#     if(n%i) == 0:
#         print("Number is not prime")
#         break
# else:
#     print("Number is prime")

n = int(input("Enter a number: "))

for num in range(2, n + 1):   # numbers from 2 to n
    for i in range(2, num):   # check divisibility
        if num % i == 0:
            break
    else:
        print(num, end=" ")



#write the Factorial of a given number

# n = int(input("Enter a number: "))
# product = 1
# for i in range(1, n+1):
#         product = product*i

# print(f"The factorial os {n} is {product}")



# #write the following star pattern like = 3

# 4



# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#         print("*"*i, end="")
#         print("")




# n = int(input("Enter a number: "))
# for i in range(1, n+1):
#     if(i==1 or i==n):
#         print("*"*n, end="")
#     else:
#         print("*", end="")
#         print(" "*(n-2), end="")
#         print("*", end="")
#     print("")



#print the reverse table of given number
# n = int(input("Eter a number: "))
# for i in range(1, 11):
#     print(f"{n} X {11-i} = {n*(11-i)}")