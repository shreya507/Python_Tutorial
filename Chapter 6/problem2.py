p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "Click this"

message = input("Enter your comment: ")

if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This is a spam")
else:
    print("This comment is not a spam")



username = input("Enter username: ")
if(len(username)<10):
    print("Your username contains less than 10 characters")
else:
    print("Your username contains more than or equal to 10 characters")


if("shruti".lower() in username.lower()):
    print("This username is niceee")