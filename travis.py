users = ["Chris","Jim","Cole","Caleigh","Rob","Heather","Monkey"]

print("There are " + str(len(users)) + " known users.")
print(users)

while True:
    print("Hi! My name is Travis.")
    name = input("What is your name?: ").strip().capitalize()

    if name in users:
        print("Hello {}!".format(name))
        remove = input("Would you like to be removed from the system (y/n)?: ").strip().lower()
        if remove == "y":
            users.remove(name) #removes the first occurance in the list
            print(users)
    elif name == "Exit":
        break
    else:
        print("Hello {}!".format(name))
        add = input("Would you like to be added the system (y/n)?: ").strip().lower()
        if add == "y":
            users.append(name) #adds the name to the list
            print(users)

users.sort()
print(users)
position = input("Which element position would you like removed (1-{})?: ".format(len(users))).strip()
del users[(int(position)-1)]
print(users)
