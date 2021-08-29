# Simple Araay

from array import*
arr = array('i',[10,20,30])
print(arr)

# Specific Element

a = array('i',[12,25,56,65])
print(a[2])

# append

arr = array('i',[45,76,32])
arr.append(56)
print(arr)


# Extend

a = array('i',[23,44,66,33,88,68])
a.extend([65,767,67,88,39])
print(a)

a = array('i',[45,77,2,8])
b = array('i',[5,9,66,43])
c = a+b
print('array = ',c)

# pop()

a = array('i',[65,76,54,77])
a.pop()
print(a)

b = array('i',[2,4,6,8,10])
print(b.pop(2))

#remove

c = array('d',[2.3,4.5,6.5,5.6])
c.remove(6.5)
print(c)

#slicing

arr = array('i',[43,66,87,35,97,55,65,88,34,78,55])
print(arr[0:4])