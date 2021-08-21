#table of 5
num = 5
for i in range(1,11):
    print(num,"X",i,"=",num * i)

#character or alphabet
a = input("Enter your Character : ")
if((a >= 'a' and a <= 'z') or (a >= 'A' and a <='Z')):
    print("The Given Character", a, "is an Alphabet")
else:
    print("The Given Character",a,"is Not an alphabet")

#numbers from 30 to 10
b=list(range(30,10,-1))
print(b)

#to check vowel or consonant
a = input("Enter a character : ")
if(a=='A' or a=='a' or a=='E' or a=='e' or a=='I' or a=='i' or a=='O' or a=='o'):
    print(a,"is vowel")
else:
    print(a,"is consonant")

#grade system
a = int(input('Enter your marks : '))
if a < 25:
    print('F')
elif a >= 25 and a < 45:
    print('E')
elif a >= 45 and a < 50:
    print('D')
elif a >= 50 and a < 60:
    print('C')
elif a >= 60 and a < 80:
    print('B')
elif a >= 80 and a < 100:
    print('A')

