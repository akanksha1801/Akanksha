#average
i = 0
sum = 0
n = int(input("Enter number : "))
while i<=n:
    sum+=i
    i+=1
print(f"sum of numbers from 0 to {n}={sum} ")
print(f"average = {sum/n}")


#multiplication table
number = int(input("Enter the Number : "))
count = 1
print("The multiplication table of : ",number)
while count <= 10:
    number = number*1
    print(number,'x','=',number*count)
    count+=1

#factorial
number = int(input("Enter a number : "))
factorial = 1
i = 1
while (i<=number):
    factorial = factorial * i
    i=i+1
    print("The factorial of",number,"is",factorial)
