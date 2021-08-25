#multiplication
def mul(numbers):
    total = 1
    for m in numbers:
        total*=m
    return total

print(mul((8,5,6)))

#reversing a string 4321abcd

def reverse_string(str):
    str1 =""
    for i in str:
        str1 = i+str1
    return str1

str = "4321abcd"
print("The original string is : ",str)
print("The reverse string is : ",reverse_string(str))

#reversing a string dcba1234

def reverse_string(str):
    str1 =""
    for i in str:
        str1 = i+str1
    return str1

str = "dcba1234"
print("The original string is : ",str)
print("The reverse string is : ",reverse_string(str))

