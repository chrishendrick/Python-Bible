a = 100 # a is global in scope

def f1():
    b = 200 # b is local in scope - within the function
    a = 50
    global c
    c = 75
    print(a+b)

def f2():
    a = 50 # creates a local variable with local scope / same name
    #print(b) will create an error as b is local to f1
    print(a)
    print(c) # c is accessible because of the global call in f1

# local variables are destroyed once the function completes
# functions will prefer local variables to global if present

def f3():
    global a #redefines global a
    a = 125
    print(a)
    
f1()
f2()
print(a) #takes the global value, not the local value in f2
f3()
print(a) #now prints the value redefined in f3
