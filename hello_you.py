# ask user for name

name = input('What is your name? ').strip()

# ask user for age
# all inputs are captured as strings, regardless of data

age = input('How old are you, ' + name + '? ').strip()

# ask user for city

city = input(name + ', what town do you live in? ').strip()

# ask user for hobby

love = input('What do you do for fun, ' + name +'? ').strip()

# create output text

print((name +' ')*3)
num1 = 11
print('Our amps go to ' + str(num1))

wholestring = 'Your name is {} and you are {} years old.  You live in {} and you love {}.'
output = wholestring.format(name, age, city, love)

# print output to screen

print(output)

print('There are ' + str(output.count("e")) + ' e characters in that sentence.')
print(output.upper()) #all upper case
print(output.lower()) #all lower case
print(output.title()) #capitalize the first letter of each word
print(output.capitalize()) #capitalize only the first word

print(output.islower()) #is everything lower case
print(output.isupper()) #is everything upper case
print(output.isalpha()) #only letters? - spaces arent letters
print(output.isdigit()) #only numbers, no spaces
print(output.isalnum()) #only letters or numbers, no spaces
#all of these are false for this string

print(output.index("years")) #print the position if string found, end on not found
print(output.find("years")) #print the position if string found, continue if not found, returns -1 if not found

string1 = "0000monkey0000"
print(string1)
print(string1.strip("0")) #if you dont include a value, it will strip spaces

