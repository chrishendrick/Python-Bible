# get sentence from user

original = input("Please enter a sentence: ").strip().lower()

# split sentence into words

words = original.split()
print(words)

# loop through words and convert to pig latin

new_words = []

for word in words:
    # if starts with vowel, just add 'yay'
    if word[0] in "aeiou": 
        new_word = word + "yay"
        new_words.append(new_word)
    else:
    # else, move the first consonant cluster to the end and add 'ay'
        vowel_pos = 0
        for letter in word:
            if letter not in "aeiou":
                vowel_pos = vowel_pos + 1
            else:
                break
        cons = word[:vowel_pos]
        #print(cons)
        the_rest = word[vowel_pos:]
        #print(the_rest)
        new_word = the_rest + cons + "ay"
        #print(new_word)
        new_words.append(new_word)
                
# stick words back together

output = " ".join(new_words) 

# output the final string

print(output)
