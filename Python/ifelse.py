#1
a = int(input('Enter the value of a : '))

if a%2==0:
    print("It is even number")
else:
    print("It is odd number")

#2
person1 = int(input("Enter age of person1 : ")) 
person2 = int(input("Enter age of person2 : ")) 
person3 = int(input("Enter age of person3 : ")) 

#oldest
if person1 > person2 and person1 > person3:
    print("Person 1 is oldest")
elif person2 > person1 and person2 > person3:
    print("Person 2 is oldest")
elif person3 > person1 and person3 > person2:
    print("Person 3 is oldest")

#youngest
if person1 < person2 and person1 < person3:
    print("Person 1 is youngest")
elif person2 < person1 and person2 < person3:
    print("Person 2 is youngest")
elif person3 < person1 and person3 < person2:
    print("Person 3 is youngest")

#3
side=[5,4,7,8,9,3,8,2,6,4]
for a in side:
    print(f"area of side {a} is {a*a}")