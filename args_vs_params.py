def about(name,age,likes = "Python"): # sets a default value for 'likes', must go last
    sentence = "Meet {}! He is {} years old and he likes {}.".format(name,age,likes)
    return sentence

print(about("Jack",23,"Football")) # assumes an order
print(about(age = 23, name = "Jack", likes = "Sausage")) # define input
print(about("Jack",23)) #uses the default value

    
