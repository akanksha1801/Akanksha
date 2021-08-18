#addition
a=20
b=10
a+=b
print(a)

#substraction
a=20
b=10
a-=b
print(a)

#multiplication
x=15
y=15
x*=y
print(x)

#division
x=20
y=5
x/=y
print(x)

#modulus
a=50
b=10
a%=b
print(a)

#floor divide
a=50
b=10
a//=b
print(a)

#exponent
a=3
b=2
a**=b
print(a)

#logical
#AND

a=-20
b=20
c=15
d=10

result=a>b and b>c and c>d
print('result=',result)

result2=a<b and b<c and c>d
print('result2=',result2)

result3=a<b and b>c and c>d
print('result3=',result3)

#OR

a=10
b=-20
c=40
d=15

result_1=a>b or b>c or c>d
print('result_1=',result_1)

result_2=a<b or b<c or c<d
print('result_2=',result_2)

result_3=a<b or b>c or c<d
print('result_3=',result_3)

#NOT

x=1
print(not x)

y=0
print(not y)



