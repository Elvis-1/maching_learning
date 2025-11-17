values = {1,2,3,"Hello",(1,2)}

print(hash((1,2)))

print(hash(("one","two",[1,2])))

set1 = {1,2,3,4,5,6,[7,8]} # you can't  add an unhashable object(list) into a set
tuple1 =(1,2,3,4,5,6)
list1 = [1,2,3,4,5,6]

set1.add(7) # mutable
# set[2] # not ordered - not subscriptable

# tuple. # not mutable
tuple1[2] # ordered - subscriptable

list1.append(7) # mutable and ordered
# print(hash(set1))


#print(set1)