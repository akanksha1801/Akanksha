#binary AND
a=18
b=11
print(a & b)

#binary OR
a=18
b=11
print(a | b)

#binary X-OR
a=18
b=11
print(a^b)

#1's Complement
a=18
print(~a)

a=-18
print(~a)

#Left Shift
a=18
b=2
print(a<<b)

#Right Shift
a=18
b=2
print(a>>b)

#Membership in
list=[18,11,2,27]
x=11
y=20
print(x in list)
print(y in list)

#not
list=[15,34,76,34]
x=34
y=36
print(x not in list)
print(y not in list)

str="Python is simple language"
print("simple" in str )
print("in" in str)

#identity
a=18
b=18
print(a is b)

a=15
b=23
print(a is b)

a=10
b='10'
print(a is not b)
