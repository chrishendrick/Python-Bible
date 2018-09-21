list = [0,1,2,3,4,5,6,7,8,9]
print(list[-1]) #last element
print(list[-2]) #2nd to last
print(list[0])  #first
print(list[0:3]) #start at 0 and pring up to (but not including) 3

nestlist = [0,1,2,[3,4,5],6,7,8,9]
print(nestlist[3])
print(nestlist[3][1])
print(nestlist[3][0::2]) #start at 0, to end, steps of 2

table = [[0,1,2],[3,4,5],[6,7,8]]
print(table[1])
print(table[1][2])

listwow = ["lists","can","have","mixed","data","types",1,2,3,4]
print(listwow[0:6])

