# cinema ticketing
# working with dictionaries, while loops, if/elif/else

# "name":[age,tickets]

films = {
    "The Big Lebowski":[17,5],
    "Bourne Identity":[18,5],
    "Tarzan":[15,3],
    "Ghost Busters":[12,5]
    }

while True:
    choice = input("Which film would you like to watch?: ").strip().title()

    if choice in films:
        #check number of tickets left
        num_seats = films[choice][1]
        if num_seats > 1:
            print("Great, there are {} seats left!".format(films[choice][1]))
        elif num_seats == 1:
            print("Great, there is {} seat left!".format(films[choice][1]))
        else:
            print("Sorry, we are sold out!")
            continue #moves to the next iteration in the while loop
        #check user age
        age = int(input("How old are you?: ").strip())
        if age >= films[choice][0]:
            print("Enjoy the film!")
            films[choice][1] = films[choice][1] - 1
        else:
            print("You're not old enough!")
    elif choice == "Exit":
        break
    else:
        print("We don't have that film...")


    
