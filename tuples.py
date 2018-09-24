#tuples are immutable
#can't change the individual elements
#lists on the other hand, are mutable
#our_tuple[2] = 6 won't work after our_tuple has been defined

our_tuple = (1,2,3,"A","B","C")
print(our_tuple[0:3])

D,E,F = [1,2,3]
G,H,I = "789"

print(D,E,F,G,H,I)
