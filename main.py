password = input("What is your password? ")
if password == "swordfish":
    print("Access granted. ")
elif password != "swordfish":
    print("it swims in the water. Please try again. ")
    if password != "swordfish":
        print("Incorrect password. You have one more try.")
        password = input("What is your password? ")
        if password == "swordfish":
            print("Access granted")
        else:
            print("You have been locked out.")
    else:
        ("Access granted.")
else:
    print("Access denied. Please retry password.")
# testing my commit. 
