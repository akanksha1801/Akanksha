#x = int(input("Enter number : "))
#y = int(input("Enter number : "))
#print(x/y)

x = int(input("Enter number : "))
y = int(input("Enter number : "))
try:
    print(x/y)
except Exception:
    print("You can not divide by zero")

x = int(input("Enter number : "))
y = int(input("Enter number : "))
try:
    print("Open resource")
    print(x/y)
except Exception as e:
    print("You can not divide by zero")
finally:
    print("Close resource")


