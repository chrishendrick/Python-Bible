for x in range (1,11,2): #iterate 1-10, not 11, by step 2
    print(x)

for letter in "asdfghjkl": #iterate letters in a string
    print(letter)

vowels = 0
consonants = 0

text = "Hello"

for letter in text:
    if letter.lower() in "aeiou":
        vowels = vowels + 1
    elif letter == " ":
        pass
    else:
        consonants = consonants + 1

print("The word is {}.".format(text))
print("There are {} vowels.".format(vowels))
print("There are {} consonants.".format(consonants))


# define a dict data type
students ={
    "male":["Tom","Charlie","Harry","Frank"],
    "female":["Sarah","Huda","Samantha","Emily","Liza"]
    }

for key in students.keys(): # for each key (male, female)
    for name in students[key]: # for each name in that key
        if "a" in name: # if there's an 'a' in the name
            print(name)
