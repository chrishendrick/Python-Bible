#collect email address

word = 'hellotheremonkey'
print(word[0])
print(word[1])
print(word[5:10:1]) #start:end:step
print(word[5:]) #from start all the way to the end
print(word[5::2]) #from start to the end by 2s position
print(word[:5]) #print up to end but not including
print(word[::-1]) #print the string backwards
print(word[-3]) #3 positions from the end of the string


email = input('What is your email address? ').strip()
error1 = email.find("@")
print(error1)

username = email[:email.index("@")]
domain = email[email.index("@")+1:]
output = "Your username is {} and your domain name is {}".format(username,domain)
print(output)
