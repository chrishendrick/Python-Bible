x=1
while x <= 10:
    if x%2 == 0: # divisible by 2 with a zero remainder i.e. even numbers
        print(x)
    x = x+1

list = [] #empty list

while len(list) < 3:
    new_name = input("Please add a new name: ").strip().capitalize()
    list.append(new_name)

print(list)
print("Sorry, list is full.")
