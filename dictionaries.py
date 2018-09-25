#Working with dictionaries data type
#key : value pairs
# denoted by {}
# dictionaries don't have an order, dont have an index - access vie key

students = {"Alice":25,"Bob":27,"Chris":41,"Dan":33,"Emma":67}
print(students["Alice"])

students["Fred"] = 66
print(students)

students["Chris"] = 42
print(students)

del students["Fred"]
print(students)

students.keys() #lists all the keys, not indexable - no [position] but...

a = list(students.keys())
print(a[1])

print(students.values())

print(students.items())
